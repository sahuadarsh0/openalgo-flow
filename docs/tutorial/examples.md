# Example Workflows

Ready-to-use workflow examples for common trading scenarios.

---

## Table of Contents

1. [Basic Examples](#basic-examples)
2. [Intraday Strategies](#intraday-strategies)
3. [Options Strategies](#options-strategies)
4. [Alert Systems](#alert-systems)
5. [Webhook Integrations](#webhook-integrations)
6. [Portfolio Management](#portfolio-management)

---

## Basic Examples

### Example 1: Simple Market Order

**Purpose**: Place a market order at a specific time.

```
Schedule (9:30 AM, Daily)
    │
    ▼
Place Order
    - Symbol: RELIANCE
    - Exchange: NSE
    - Action: BUY
    - Quantity: 10
    - Product: MIS
    - Price Type: MARKET
    - Output: orderResult
    │
    ▼
Telegram Alert
    - Message: "Bought 10 RELIANCE @ {{orderResult.price}}"
```

---

### Example 2: Time-Based Entry and Exit

**Purpose**: Enter at market open, exit before close.

```
Schedule (9:15 AM, Daily)
    │
    ▼
Wait Until (9:30)
    │
    ▼
Place Order (BUY)
    - Symbol: NIFTY25JANFUT
    - Exchange: NFO
    - Action: BUY
    - Quantity: 75
    - Product: MIS
    │
    ▼
Wait Until (15:15)
    │
    ▼
Close Positions
    - Product: MIS
    │
    ▼
Telegram Alert
    - Message: "All MIS positions closed"
```

---

### Example 3: Conditional Order

**Purpose**: Only buy if funds are sufficient.

```
Schedule (9:30 AM)
    │
    ▼
Fund Check
    - Minimum: 50000
    │
    ├── Yes ──► Place Order (BUY RELIANCE)
    │               │
    │               ▼
    │           Telegram Alert ("Order placed")
    │
    └── No ──► Telegram Alert ("Insufficient funds")
```

---

## Intraday Strategies

### Example 4: Market Hours Only Trading

**Purpose**: Only trade during market hours.

```
Schedule (Every 5 minutes)
    │
    ▼
Time Window
    - Start: 09:30
    - End: 15:15
    │
    ├── Yes ──► Get Quote (NIFTY)
    │               │
    │               ▼
    │           Price Condition (LTP > 24000)
    │               │
    │               ├── Yes ──► Place Order (BUY)
    │               │
    │               └── No ──► Log ("Price below threshold")
    │
    └── No ──► Log ("Outside market hours")
```

---

### Example 5: Scalping with Multiple Conditions

**Purpose**: Enter when multiple conditions align.

```
Schedule (Every 1 minute)
    │
    ▼
Get Quote (BANKNIFTY) → niftyQuote
    │
    ▼
┌─────────────────────────────────┐
│         AND Gate (3 inputs)     │
│                                 │
│ Input 1: Time Condition (>=9:30)│
│ Input 2: Price > 52000          │
│ Input 3: Position Check (No Pos)│
└────────────────┬────────────────┘
                 │
    ├── Yes ──► Options Order
    │               - Underlying: BANKNIFTY
    │               - Type: CE, ATM
    │               - Action: BUY
    │               │
    │               ▼
    │           Variable (entryPrice)
    │               - Set: {{niftyQuote.data.ltp}}
    │
    └── No ──► Log ("Conditions not met")
```

---

### Example 6: Stop Loss and Target

**Purpose**: Place order with SL and target monitoring.

```
Schedule (9:30 AM)
    │
    ▼
Place Order (BUY SBIN)
    - Quantity: 100
    - Output: entryOrder
    │
    ▼
Get Quote (SBIN) → quote
    │
    ▼
Variable (entryPrice)
    - Set: {{quote.data.ltp}}
    │
    ▼
Variable (stopLoss)
    - Set: {{entryPrice}}
    - Operation: Multiply
    - Value: 0.99  (1% SL)
    │
    ▼
Variable (target)
    - Set: {{entryPrice}}
    - Operation: Multiply
    - Value: 1.02  (2% Target)
    │
    ▼
Telegram Alert
    - Message: "Entry: {{entryPrice}}, SL: {{stopLoss}}, Target: {{target}}"
```

---

## Options Strategies

### Example 7: Short Straddle at 9:30

**Purpose**: Sell ATM straddle at market open.

```
Schedule (9:15 AM, Weekdays)
    │
    ▼
Wait Until (9:30)
    │
    ▼
Multi-Leg Options
    - Strategy: Straddle
    - Underlying: NIFTY
    - Expiry: Current Week
    - Action: SELL
    - Quantity: 1 lot
    - Product: MIS
    - Output: straddleOrder
    │
    ▼
Telegram Alert
    - Message: "Straddle sold - {{straddleOrder.results}}"
    │
    ▼
Wait Until (15:15)
    │
    ▼
Close Positions
    - Product: MIS
```

---

### Example 8: Iron Condor with Alerts

**Purpose**: Deploy iron condor and monitor.

```
Schedule (9:45 AM, Weekly: Mon)
    │
    ▼
Fund Check (Minimum: 100000)
    │
    ├── Yes ──► Multi-Leg Options
    │               - Strategy: Iron Condor
    │               - Underlying: NIFTY
    │               - Expiry: Current Week
    │               - Action: SELL
    │               - Output: icOrder
    │               │
    │               ▼
    │           Telegram Alert
    │               - Message: "Iron Condor deployed!"
    │
    └── No ──► Telegram Alert ("Need 1L margin for IC")
```

---

### Example 9: Dynamic Options Based on Signal

**Purpose**: Buy options based on webhook signal.

```
Webhook Trigger
    │
    ▼
Variable (direction)
    - Get: webhook.direction
    │
    ▼
┌─────────────────────────────────┐
│      {{webhook.direction}}      │
│                                 │
│    ┌──────────┬──────────┐     │
│    │          │          │     │
│  BULLISH   BEARISH   NEUTRAL   │
│    │          │          │     │
│    ▼          ▼          ▼     │
│  Buy CE    Buy PE    Straddle  │
└─────────────────────────────────┘
```

---

## Alert Systems

### Example 10: Price Breakout Alert

**Purpose**: Alert on price breakout.

```
Price Alert
    - Symbol: RELIANCE
    - Condition: Crossing Up
    - Price: 3000
    │
    ├── Yes ──► Telegram Alert
    │               - Message: "RELIANCE crossed 3000! LTP: {{quote.data.ltp}}"
    │
    └── No ──► (continues monitoring)
```

---

### Example 11: Multi-Symbol Watchlist

**Purpose**: Monitor multiple stocks.

```
Schedule (Every 5 minutes, Market Hours)
    │
    ▼
Multi Quotes
    - Symbols: RELIANCE,INFY,TCS,HDFCBANK,SBIN
    - Output: watchlist
    │
    ▼
Log (Info)
    - Message: "Watchlist: {{watchlist.results}}"
    │
    ▼
HTTP Request
    - Method: POST
    - URL: https://your-dashboard.com/api/update
    - Body: {{watchlist}}
```

---

### Example 12: P&L Monitor

**Purpose**: Alert on P&L thresholds.

```
Schedule (Every 1 minute)
    │
    ▼
Open Position
    - Symbol: NIFTY
    - Exchange: NFO
    - Output: position
    │
    ▼
┌─────────────────────┐
│      OR Gate        │
│                     │
│ P&L > 5000 (profit) │
│ P&L < -2000 (loss)  │
└──────────┬──────────┘
           │
    ├── Yes ──► Close Positions
    │               │
    │               ▼
    │           Telegram Alert
    │               - Message: "Position closed. P&L: {{position.pnl}}"
    │
    └── No ──► (continue monitoring)
```

---

## Webhook Integrations

### Example 13: TradingView Alert Handler

**Purpose**: Execute orders from TradingView alerts.

```
Webhook Trigger
    │
    ▼
Log (Info)
    - Message: "Received: {{webhook}}"
    │
    ▼
Place Order
    - Symbol: {{webhook.symbol}}
    - Exchange: {{webhook.exchange}}
    - Action: {{webhook.action}}
    - Quantity: {{webhook.quantity}}
    - Product: MIS
    - Output: order
    │
    ▼
Telegram Alert
    - Message: "TV Alert executed: {{webhook.action}} {{webhook.symbol}}"
```

**TradingView Alert Message**:
```json
{
  "symbol": "RELIANCE",
  "exchange": "NSE",
  "action": "BUY",
  "quantity": 10
}
```

---

### Example 14: ChartInk Scanner Integration

**Purpose**: Trade based on ChartInk scanner results.

```
Webhook Trigger
    │
    ▼
Variable (scanResults)
    - Get: webhook.stocks
    │
    ▼
Log (Info)
    - Message: "Scanner found: {{scanResults}}"
    │
    ▼
Basket Order
    - Orders: {{scanResults}}
    - Product: MIS
    │
    ▼
Telegram Alert
    - Message: "Executed {{scanResults.length}} trades from scanner"
```

---

### Example 15: External API Signal

**Purpose**: Trade based on external ML model.

```
Schedule (9:25 AM)
    │
    ▼
HTTP Request
    - Method: GET
    - URL: https://your-ml-api.com/predict
    - Output: prediction
    │
    ▼
Variable (signal)
    - Get: prediction.data.signal
    │
    ▼
Price Condition ({{signal}} == "BUY")
    │
    ├── Yes ──► Place Order (BUY)
    │
    └── No ──► Log ("No buy signal")
```

---

## Portfolio Management

### Example 16: SIP Automation

**Purpose**: Systematic investment on schedule.

```
Schedule (1st of every month, 10:00 AM)
    │
    ▼
Fund Check (Minimum: 10000)
    │
    ├── Yes ──► Basket Order
    │               - Orders:
    │                   NIFTYBEES,NSE,BUY,10
    │                   GOLDBEES,NSE,BUY,5
    │                   LIQUIDBEES,NSE,BUY,10
    │               - Product: CNC
    │               │
    │               ▼
    │           Telegram Alert ("SIP executed for the month")
    │
    └── No ──► Telegram Alert ("SIP failed - insufficient funds")
```

---

### Example 17: Rebalancing

**Purpose**: Quarterly portfolio rebalancing.

```
Schedule (Quarterly: Jan, Apr, Jul, Oct - 1st)
    │
    ▼
Close Positions
    - Product: CNC
    │
    ▼
Delay (5 minutes)
    │
    ▼
Basket Order
    - Orders: (rebalanced portfolio)
    - Product: CNC
    │
    ▼
Telegram Alert
    - Message: "Portfolio rebalanced"
```

---

### Example 18: End of Day Summary

**Purpose**: Daily P&L summary.

```
Schedule (15:45, Weekdays)
    │
    ▼
Open Position
    - Symbol: ALL
    - Output: positions
    │
    ▼
HTTP Request
    - Method: POST
    - URL: https://your-dashboard.com/eod
    - Body: {"positions": {{positions}}, "date": "{{date}}"}
    │
    ▼
Telegram Alert
    - Message: "EOD Summary for {{date}}: Total P&L: {{positions.total_pnl}}"
```

---

## Tips for Building Workflows

1. **Start Simple**: Begin with basic workflows and add complexity

2. **Test First**: Always use "Run Now" before activating

3. **Add Logging**: Include Log nodes to track execution

4. **Use Variables**: Store intermediate values for later use

5. **Error Handling**: Add Telegram alerts for failures

6. **Time Windows**: Restrict trading to market hours

7. **Fund Checks**: Verify funds before placing orders

8. **Position Checks**: Avoid duplicate entries

---

## Contributing Examples

Have a great workflow? Share it!

1. Export your workflow
2. Create a GitHub issue or PR
3. Include:
   - Strategy description
   - Use case
   - Configuration notes
   - Disclaimer
