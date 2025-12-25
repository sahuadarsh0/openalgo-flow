# Supported Brokers

OpenAlgo Flow works with **25+ Indian brokers** through the unified OpenAlgo API. All brokers share the same API interface, making it easy to switch between brokers without changing your workflow.

---

## Complete Broker List

| # | Broker | Variants | Exchanges |
|---|--------|----------|-----------|
| 1 | **5paisa** | Standard, XTS | NSE, BSE, NFO, MCX |
| 2 | **AliceBlue** | Standard | NSE, BSE, NFO, MCX, CDS |
| 3 | **AngelOne** | Standard | NSE, BSE, NFO, MCX, CDS |
| 4 | **Compositedge** | Standard | NSE, BSE, NFO |
| 5 | **Definedge** | Standard | NSE, BSE, NFO |
| 6 | **Dhan** | Live, Sandbox | NSE, BSE, NFO, MCX, CDS |
| 7 | **Firstock** | Standard | NSE, BSE, NFO |
| 8 | **Flattrade** | Standard | NSE, BSE, NFO, MCX, CDS |
| 9 | **Fyers** | Standard | NSE, BSE, NFO, MCX, CDS |
| 10 | **Groww** | Standard | NSE, BSE |
| 11 | **IBulls** | Standard | NSE, BSE, NFO |
| 12 | **IIFL** | Standard | NSE, BSE, NFO, MCX |
| 13 | **Indmoney** | Standard | NSE, BSE |
| 14 | **JainamXTS** | Standard | NSE, BSE, NFO |
| 15 | **Kotak Neo** | Standard | NSE, BSE, NFO, MCX, CDS |
| 16 | **Motilal Oswal** | Standard | NSE, BSE, NFO, CDS |
| 17 | **Mstock** | Standard | NSE, BSE, NFO |
| 18 | **Paytm Money** | Standard | NSE, BSE, NFO |
| 19 | **Pocketful** | Standard | NSE, BSE, NFO |
| 20 | **Samco** | Standard | NSE, BSE, NFO, MCX |
| 21 | **Shoonya (Finvasia)** | Standard | NSE, BSE, NFO, MCX, CDS |
| 22 | **Tradejini** | Standard | NSE, BSE, NFO |
| 23 | **Upstox** | Standard | NSE, BSE, NFO, MCX, CDS |
| 24 | **Wisdom Capital** | Standard | NSE, BSE, NFO |
| 25 | **Zebu** | Standard | NSE, BSE, NFO, MCX |
| 26 | **Zerodha** | Standard | NSE, BSE, NFO, MCX, CDS |

---

## Unified API Interface

All brokers share the same API methods, so your workflows work with any broker:

| Function | Description |
|----------|-------------|
| `placeorder()` | Place market/limit orders |
| `placesmartorder()` | Position-aware orders |
| `modifyorder()` | Modify existing orders |
| `cancelorder()` | Cancel an order |
| `cancelallorders()` | Cancel all open orders |
| `closeposition()` | Close specific position |
| `closeallpositions()` | Close all positions |
| `orderbook()` | Get all orders |
| `tradebook()` | Get executed trades |
| `positionbook()` | Get open positions |
| `holdings()` | Get stock holdings |
| `funds()` | Get available funds |
| `quotes()` | Get real-time quotes |
| `depth()` | Get order book depth |
| `history()` | Get historical data |
| `expiry()` | Get F&O expiry dates |

---

## Exchange Support

### Equity Exchanges

| Exchange | Code | Description |
|----------|------|-------------|
| National Stock Exchange | `NSE` | Primary equity exchange |
| Bombay Stock Exchange | `BSE` | Secondary equity exchange |
| NSE Index | `NSE_INDEX` | Index quotes (NIFTY, etc.) |
| BSE Index | `BSE_INDEX` | BSE index quotes |

### Derivatives Exchanges

| Exchange | Code | Description |
|----------|------|-------------|
| NSE F&O | `NFO` | NSE derivatives |
| BSE F&O | `BFO` | BSE derivatives |
| Currency | `CDS` | Currency derivatives |
| BSE Currency | `BCD` | BSE currency derivatives |
| Commodity | `MCX` | Multi Commodity Exchange |

---

## Product Types

| Product | Code | Description |
|---------|------|-------------|
| Intraday | `MIS` | Margin Intraday Square-off |
| Delivery | `CNC` | Cash & Carry (Equity) |
| Normal | `NRML` | Overnight F&O positions |

---

## Price Types

| Type | Code | Description |
|------|------|-------------|
| Market | `MARKET` | Execute at current price |
| Limit | `LIMIT` | Execute at specified price |
| Stop Loss | `SL` | Limit order with trigger |
| Stop Loss Market | `SL-M` | Market order with trigger |

---

## Broker-Specific Features

### Dhan

- **Sandbox Mode**: Test without real money
- Enable sandbox in Dhan app settings
- Same API, simulated execution

### 5paisa

- **Standard**: Regular API
- **XTS**: Advanced trading platform

### Zerodha

- Most popular broker in India
- Full exchange support
- Advanced order types

### Angel One

- Previously known as Angel Broking
- SmartAPI integration
- Free trading API

### Fyers

- Developer-friendly API
- Good documentation
- Supports all exchanges

---

## How to Connect Your Broker

### Step 1: Setup OpenAlgo

1. Install [OpenAlgo](https://github.com/marketcalls/openalgo)
2. Configure your broker credentials
3. Start the OpenAlgo server

### Step 2: Get API Key

1. Login to OpenAlgo web interface
2. Navigate to API Keys
3. Generate a new API key
4. Copy the key

### Step 3: Configure OpenAlgo Flow

1. Open OpenAlgo Flow
2. Go to **Settings**
3. Enter:
   - **API URL**: Your OpenAlgo server URL
   - **API Key**: The key you generated
4. Click **Test Connection**
5. Click **Save Settings**

---

## Switching Brokers

Since all brokers use the same API:

1. Your workflows remain unchanged
2. Simply reconnect OpenAlgo to a different broker
3. OpenAlgo Flow automatically uses the new broker

**No code changes required!**

---

## Symbol Naming

Use the exact symbol name as it appears on the exchange:

### Equity
```
RELIANCE   (not Reliance Industries)
INFY       (not Infosys)
TCS        (not Tata Consultancy)
SBIN       (not State Bank)
```

### F&O (Options)
OpenAlgo Flow automatically constructs option symbols:
```
Underlying: NIFTY
Expiry: Current Week
Strike: ATM
Type: CE

→ Automatically becomes: NIFTY25JAN24500CE
```

### F&O (Futures)
```
NIFTY25JANFUT
BANKNIFTY25JANFUT
```

---

## Best Practices

1. **Use Sandbox First**: Test with Dhan sandbox before live trading

2. **Check Market Hours**: Ensure your broker session is active

3. **Verify Funds**: Check available margin before placing orders

4. **Use Correct Exchange**: NSE for stocks, NFO for options

5. **Symbol Spelling**: Use exact symbol names

---

## Common Issues

### "Invalid Symbol" Error

- Check symbol spelling (must be exact)
- Verify correct exchange is selected
- Ensure symbol is tradeable

### "Session Expired" Error

- Re-login to your broker in OpenAlgo
- Refresh the broker session
- Check if market hours are active

### "Insufficient Margin" Error

- Check available funds
- Reduce order quantity
- Verify product type (MIS vs CNC)

### "Order Rejected" Error

- Check market hours
- Verify price limits (circuit breakers)
- Check lot size for F&O

---

## Getting Help

- **OpenAlgo Documentation**: [https://docs.openalgo.in](https://docs.openalgo.in)
- **Broker API Docs**: Check your broker's developer portal
- **GitHub Issues**: Report problems on the repository
