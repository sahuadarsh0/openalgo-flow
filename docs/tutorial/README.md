# OpenAlgo Flow - Complete Tutorial

**Visual Trading Automation for Indian Markets**

OpenAlgo Flow is a powerful no-code trading automation platform that lets traders and investors create, test, and deploy algorithmic trading strategies using a visual drag-and-drop interface. Built on top of the OpenAlgo API, it supports 25+ Indian brokers with a unified interface.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Who is this for?](#who-is-this-for)
3. [Key Features](#key-features)
4. [Quick Start](#quick-start)
5. [Documentation](#documentation)

---

## Introduction

OpenAlgo Flow transforms complex trading logic into simple visual workflows. Instead of writing code, you connect nodes on a canvas to build your trading strategy. Each node represents an action, condition, or data operation.

**Example Workflow:**
```
Schedule (9:15 AM)
    → Time Condition (>= 9:30)
        → Place Order (BUY NIFTY)
            → Telegram Alert ("Order placed!")
```

This simple workflow:
- Starts at 9:15 AM
- Waits until 9:30 AM
- Places a BUY order for NIFTY
- Sends a Telegram notification

---

## Who is this for?

### Traders
- **Intraday Traders**: Automate entry/exit based on time, price, or conditions
- **Options Traders**: Execute complex multi-leg strategies (Straddle, Strangle, Iron Condor)
- **Swing Traders**: Set up price alerts and automated position management

### Investors
- **SIP Automation**: Schedule regular investments
- **Portfolio Rebalancing**: Automate basket orders
- **Alert Systems**: Get notified on price movements

### Algo Enthusiasts
- **Strategy Prototyping**: Quickly test trading ideas
- **Paper Trading**: Test in sandbox mode before going live
- **Webhook Integration**: Connect to TradingView, ChartInk, or custom signals

---

## Key Features

| Feature | Description |
|---------|-------------|
| **Visual Builder** | Drag-and-drop node-based workflow editor |
| **25+ Brokers** | Unified API across all major Indian brokers |
| **Options Trading** | Built-in ATM/ITM/OTM strike selection |
| **Multi-Leg Orders** | Straddle, Strangle, Iron Condor, Spreads |
| **Scheduling** | Daily, weekly, interval-based triggers |
| **Webhooks** | External triggers from TradingView/ChartInk |
| **Variables** | Pass data between nodes dynamically |
| **Telegram Alerts** | Real-time notifications |
| **Sandbox Mode** | Test without real money |

---

## Quick Start

### 1. Setup (5 minutes)
```bash
# Clone the repository
git clone https://github.com/marketcalls/openalgo-flow.git
cd openalgo-flow

# Start backend
cd backend
uv sync
uv run uvicorn app.main:app --reload

# Start frontend (new terminal)
cd frontend
npm install
npm run dev
```

### 2. Configure OpenAlgo
1. Open `http://localhost:5173`
2. Go to **Settings**
3. Enter your OpenAlgo API URL and API Key
4. Click **Test Connection**

### 3. Create Your First Workflow
1. Click **New Workflow**
2. Drag a **Schedule** node to the canvas
3. Drag a **Place Order** node and connect them
4. Configure the order (Symbol, Exchange, Action, Quantity)
5. Click **Save** and **Activate**

---

## Documentation

| Document | Description |
|----------|-------------|
| [Getting Started](./getting-started.md) | Installation, setup, and configuration |
| [Nodes Reference](./nodes-reference.md) | Complete guide to all workflow nodes |
| [Built-in Variables](./variables.md) | Dynamic variables and interpolation |
| [Supported Brokers](./brokers.md) | List of 25+ supported brokers |
| [Keyboard Shortcuts](./keyboard-shortcuts.md) | Productivity shortcuts |
| [Sharing Strategies](./sharing-strategies.md) | Export, import, and share workflows |
| [Example Workflows](./examples.md) | Real-world strategy examples |

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    OpenAlgo Flow                         │
├─────────────────────────────────────────────────────────┤
│  Frontend (React + TypeScript)                          │
│  ├── Visual Workflow Editor (ReactFlow)                 │
│  ├── Node Palette (Drag & Drop)                         │
│  └── Configuration Panels                               │
├─────────────────────────────────────────────────────────┤
│  Backend (FastAPI + Python)                             │
│  ├── Workflow Executor                                  │
│  ├── Scheduler (APScheduler)                            │
│  └── WebSocket (Real-time updates)                      │
├─────────────────────────────────────────────────────────┤
│  OpenAlgo API                                           │
│  └── Unified interface to 25+ brokers                   │
└─────────────────────────────────────────────────────────┘
```

---

## Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/marketcalls/openalgo-flow/issues)
- **OpenAlgo Documentation**: [https://docs.openalgo.in](https://docs.openalgo.in)

---

**Version**: 1.0.0 (Genesis)
**License**: MIT
**Powered by**: OpenAlgo API
