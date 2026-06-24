

import numpy as np
import pandas as pd


class CryptoTradingEnv:
    def __init__(self, df: pd.DataFrame, window_size: int = 10,
                 transaction_cost: float = 0.001, eta: float = 0.01):
     
        self.prices = df.copy().astype(float).sort_index()
        # log-return: r_t = ln(P_t / P_{t-1})
        self.returns = np.log(self.prices / self.prices.shift(1)).dropna()
        self.returns_values = self.returns.values          
        self.dates = self.returns.index
        self.n_assets = self.returns.shape[1]
        self.window_size = window_size
        self.transaction_cost = transaction_cost
        self.eta = eta
        self.max_step = len(self.returns_values) - 1

        self.reset()

    # ------------------------------------------------------------------ #
    # API chính
    # ------------------------------------------------------------------ #
    def reset(self, start_index: int | None = None):
      
        self.t = self.window_size if start_index is None else max(self.window_size, start_index)
        self.weights = np.ones(self.n_assets) / self.n_assets   
        self.portfolio_value = 1.0
        self.A = 0.0   
        self.B = 0.0   
        self.done = False
        self.history = {
            "portfolio_value": [self.portfolio_value],
            "weights": [self.weights.copy()],
            "reward": [],
        }
        return self._get_state()

    def step(self, action):
        new_weights = self._normalize_action(action)

        # chi phí giao dịch tỷ lệ với mức thay đổi tỷ trọng (turnover)
        turnover = np.abs(new_weights - self.weights).sum()
        cost = self.transaction_cost * turnover

        asset_returns = self.returns_values[self.t]
        gross_return = float(np.dot(new_weights, asset_returns))
        portfolio_return = gross_return - cost

        self.portfolio_value *= np.exp(portfolio_return)
        reward = self._get_reward(portfolio_return)

        self.weights = new_weights
        self.t += 1
        self.done = self.t >= self.max_step

        self.history["portfolio_value"].append(self.portfolio_value)
        self.history["weights"].append(self.weights.copy())
        self.history["reward"].append(reward)

        next_state = np.zeros(self.state_size, dtype=np.float32) if self.done else self._get_state()
        info = {
            "portfolio_return": portfolio_return,
            "portfolio_value": self.portfolio_value,
            "turnover": turnover,
        }
        return next_state, reward, self.done, info

    # ------------------------------------------------------------------ #
    # Nội bộ
    # ------------------------------------------------------------------ #
    def _normalize_action(self, action):
        
        action = np.clip(np.asarray(action, dtype=float), 0, None)
        total = action.sum()
        if total <= 1e-8:
            return np.ones(self.n_assets) / self.n_assets
        return action / total

    def _get_state(self):
        window = self.returns_values[self.t - self.window_size:self.t]
        mean = window.mean(axis=0)
        std = window.std(axis=0) + 1e-8
        norm_window = (window - mean) / std                 # z-score theo từng coin
        state = np.concatenate([norm_window.flatten(), self.weights])
        return state.astype(np.float32)

    def _get_reward(self, portfolio_return):
        delta_A = portfolio_return - self.A
        delta_B = portfolio_return ** 2 - self.B
        denom = (self.B - self.A ** 2)
        denom = denom ** 1.5 if denom > 1e-8 else 0.0
        dsr = 0.0 if denom == 0.0 else (self.B * delta_A - 0.5 * self.A * delta_B) / denom
        # cập nhật EMA sau khi đã dùng giá trị A, B của bước trước để tính reward
        self.A += self.eta * delta_A
        self.B += self.eta * delta_B
        return float(dsr)

    @property
    def state_size(self):
        return self.window_size * self.n_assets + self.n_assets


def build_discrete_action_set(n_assets: int, concentration: float = 0.8):

    actions = []
    for i in range(n_assets):
        w = np.full(n_assets, (1 - concentration) / (n_assets - 1))
        w[i] = concentration
        actions.append(w)
    actions.append(np.ones(n_assets) / n_assets)
    return np.array(actions)
