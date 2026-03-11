# Quantitative Trading Engine Simulation

A high-performance, concurrent trading engine built in **Python** to simulate real-time market dynamics. This project features a core matching engine that processes limit and market orders using a **Price-Time Priority (FIFO)** algorithm, designed for quantitative strategy backtesting and high-concurrency order execution.

## 🚀 Key Features

* **High-Concurrency Matching Engine:** Optimized for handling multiple order streams using Python’s `threading` or `asyncio` for thread-safe operations.
* **Price-Time Priority (FIFO):** Implements industry-standard execution logic where orders at the same price level are filled based on their arrival time.
* **Real-Time Order Book:** Maintains a live Limit Order Book (LOB) with efficient updates for Bids and Asks.
* **Trade Analytics:** Calculates real-time financial metrics, including **VWAP** (Volume-Weighted Average Price) and liquidity depth analysis.
* **Scalable Architecture:** Modular design allowing for easy integration of new trading strategies or data feeds.

## 🛠 Technical Stack

* **Language:** Python 3.x
* **Concurrency:** Multi-threading / AsyncIO
* **Data Analysis:** NumPy / Pandas (for metric calculations)
* **Data Structures:** Efficient use of `collections.deque` and `heapq` for $O(1)$ or $O(\log n)$ order processing.

## 📉 Core Logic & Analytics

The engine follows a standard financial exchange workflow:
1.  **Order Entry:** Validates order type (Limit/Market), side (Buy/Sell), and volume.
2.  **Matching Algorithm:** * If a match is found (Buy Price $\ge$ Sell Price), a trade is executed.
    * Unfilled orders are placed in the **Limit Order Book** prioritized by price, then timestamp.
3.  **Financial Metrics:**
    * **VWAP Calculation:** $$VWAP = \frac{\sum (Price \times Volume)}{\sum Volume}$$
    * **Spread Analysis:** Monitors the gap between the best Bid and best Ask.

## 🏁 Quick Start
python main.py
