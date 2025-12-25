# Built-in Variables

OpenAlgo Flow supports dynamic variable interpolation using the `{{variable}}` syntax. This allows you to pass data between nodes and access real-time values.

---

## Variable Syntax

Variables are enclosed in double curly braces:

```
{{variableName}}
{{object.property}}
{{array[0].property}}
```

---

## Built-in System Variables

These variables are always available in any node:

| Variable | Description | Example Value |
|----------|-------------|---------------|
| `{{timestamp}}` | Current ISO timestamp | `2025-01-15T09:30:00.000Z` |
| `{{date}}` | Current date (YYYY-MM-DD) | `2025-01-15` |
| `{{time}}` | Current time (HH:MM:SS) | `09:30:00` |
| `{{weekday}}` | Day of week (0=Monday) | `0` |
| `{{weekday_name}}` | Day name | `Monday` |
| `{{hour}}` | Current hour (0-23) | `9` |
| `{{minute}}` | Current minute (0-59) | `30` |

---

## Webhook Variables

When workflow is triggered via webhook, the payload is available:

| Variable | Description |
|----------|-------------|
| `{{webhook}}` | Entire webhook payload |
| `{{webhook.symbol}}` | Symbol from payload |
| `{{webhook.action}}` | Action from payload |
| `{{webhook.price}}` | Price from payload |
| `{{webhook.quantity}}` | Quantity from payload |
| `{{webhook.*}}` | Any field from payload |

**Example Webhook Payload**:
```json
{
  "symbol": "NIFTY",
  "action": "BUY",
  "price": 24500,
  "quantity": 75,
  "strategy": "momentum"
}
```

**Access in nodes**:
```
Symbol: {{webhook.symbol}}    → NIFTY
Action: {{webhook.action}}    → BUY
Price: {{webhook.price}}      → 24500
Strategy: {{webhook.strategy}} → momentum
```

---

## Node Output Variables

Each node can store its output in a variable:

### Order Nodes

**Place Order / Smart Order / Options Order**:
```
{{orderResult.orderid}}     - Order ID
{{orderResult.status}}      - Status (success/error)
{{orderResult.message}}     - Response message
{{orderResult.symbol}}      - Symbol
{{orderResult.exchange}}    - Exchange
{{orderResult.action}}      - BUY/SELL
{{orderResult.quantity}}    - Quantity
```

**Multi-Leg Options**:
```
{{multiLegOrder.results}}       - Array of leg results
{{multiLegOrder.results[0]}}    - First leg result
{{multiLegOrder.strategy}}      - Strategy name
```

**Basket Order**:
```
{{basketResult.results}}        - Array of order results
{{basketResult.results[0].orderid}} - First order ID
{{basketResult.count}}          - Number of orders
```

### Data Nodes

**Get Quote**:
```
{{quote.data.ltp}}          - Last traded price
{{quote.data.open}}         - Open price
{{quote.data.high}}         - High price
{{quote.data.low}}          - Low price
{{quote.data.prev_close}}   - Previous close
{{quote.data.volume}}       - Volume
{{quote.data.change}}       - Change amount
{{quote.data.change_percent}} - Change percentage
{{quote.data.oi}}           - Open interest (F&O)
```

**Get Depth**:
```
{{depth.data.bids[0].price}}     - Best bid price
{{depth.data.bids[0].quantity}}  - Best bid quantity
{{depth.data.asks[0].price}}     - Best ask price
{{depth.data.asks[0].quantity}}  - Best ask quantity
{{depth.data.bids[1].price}}     - Second bid price
```

**Open Position**:
```
{{position.quantity}}        - Position size
{{position.pnl}}            - Profit/Loss
{{position.average_price}}  - Average entry price
{{position.ltp}}            - Last traded price
{{position.product}}        - Product type
```

**Order Status**:
```
{{orderStatus.status}}       - Order status
{{orderStatus.filled_qty}}   - Filled quantity
{{orderStatus.pending_qty}}  - Pending quantity
{{orderStatus.price}}        - Order price
{{orderStatus.average_price}} - Fill price
```

**Expiry Dates**:
```
{{expiries.data}}           - Array of expiry dates
{{expiries.data[0]}}        - Nearest expiry
{{expiries.data[1]}}        - Next expiry
{{expiries.data[2]}}        - Third expiry
```

### HTTP Request

```
{{apiResponse.status}}      - HTTP status code (200, 404, etc.)
{{apiResponse.data}}        - Response body
{{apiResponse.success}}     - true/false
{{apiResponse.data.field}}  - Access nested response fields
```

---

## Using Variables in Nodes

### In Text Fields

Use variables directly in text inputs:

**Telegram Message**:
```
Order placed!
Symbol: {{webhook.symbol}}
Price: {{quote.data.ltp}}
Order ID: {{orderResult.orderid}}
Time: {{timestamp}}
```

**Log Message**:
```
Processing {{webhook.action}} for {{webhook.symbol}} at {{quote.data.ltp}}
```

### In Configuration Fields

**Symbol Field** (supports variable):
```
{{webhook.symbol}}
```

**Quantity Field** (supports variable):
```
{{webhook.quantity}}
```

**URL Field** (HTTP Request):
```
https://api.example.com/{{webhook.endpoint}}
```

**JSON Body** (HTTP Request):
```json
{
  "symbol": "{{webhook.symbol}}",
  "price": {{quote.data.ltp}},
  "action": "{{orderResult.status}}"
}
```

---

## Variable Operations

The **Variable** node allows mathematical and string operations:

### Set Value
```
Operation: Set
Variable: myPrice
Value: 100.50
Result: {{myPrice}} = 100.50
```

### Get from Another Variable
```
Operation: Get
Variable: currentLTP
Source: quote
JSON Path: data.ltp
Result: {{currentLTP}} = quote.data.ltp
```

### Mathematical Operations
```
Operation: Add
Variable: totalQty
Value: 10
Result: {{totalQty}} = {{totalQty}} + 10

Operation: Multiply
Variable: lotValue
Value: {{lotSize}}
Result: {{lotValue}} = {{lotValue}} * {{lotSize}}
```

### Increment/Decrement
```
Operation: Increment
Variable: counter
Result: {{counter}} = {{counter}} + 1

Operation: Decrement
Variable: remaining
Result: {{remaining}} = {{remaining}} - 1
```

---

## Nested Property Access

Access nested objects using dot notation:

```
{{quote.data.ltp}}           - Object property
{{depth.data.bids[0].price}} - Array + property
{{results[0].orders[0].id}}  - Nested arrays
```

---

## Examples

### Example 1: Dynamic Order from Webhook

**Webhook Payload**:
```json
{
  "symbol": "RELIANCE",
  "action": "BUY",
  "quantity": 10,
  "exchange": "NSE"
}
```

**Place Order Configuration**:
```
Symbol: {{webhook.symbol}}
Exchange: {{webhook.exchange}}
Action: {{webhook.action}}
Quantity: {{webhook.quantity}}
```

### Example 2: Price-Based Alert

**Workflow**:
```
Get Quote (NIFTY) → Output: niftyQuote
    ↓
Telegram Alert
    Message: "NIFTY LTP: {{niftyQuote.data.ltp}}, Change: {{niftyQuote.data.change_percent}}%"
```

### Example 3: Order Confirmation

**Workflow**:
```
Place Order → Output: myOrder
    ↓
Log (Info)
    Message: "Order {{myOrder.orderid}} {{myOrder.status}}"
    ↓
Telegram Alert
    Message: "Executed {{myOrder.action}} {{myOrder.quantity}} {{myOrder.symbol}} @ {{quote.data.ltp}}"
```

### Example 4: Conditional Variable

**Workflow**:
```
Get Quote (NIFTY) → Output: quote
    ↓
Variable (counter) → Set to 0
    ↓
Price Condition (LTP > 24000)
    ↓ Yes
    Variable (counter) → Increment
    ↓
Log: "Counter is now {{counter}}"
```

---

## Best Practices

1. **Use Descriptive Names**: `niftyQuote` instead of `q1`

2. **Check for Null**: Variables may be undefined if the node failed

3. **Store Important Data**: Use Variable node to save values for later use

4. **Use Logs for Debugging**: Log variable values to verify data

5. **Keep It Simple**: Avoid deeply nested variable access when possible

---

## Troubleshooting

### Variable Shows `{{variableName}}`

- Variable was not set or node failed
- Check previous nodes executed successfully
- Verify variable name spelling

### Variable Shows `undefined`

- Property doesn't exist on the object
- Check the exact property path
- Use Log node to inspect the full object

### Variable Shows `[object Object]`

- Trying to display an object as string
- Access specific properties: `{{obj.property}}`
- Or use stringify to see full object
