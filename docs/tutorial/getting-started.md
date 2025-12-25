# Getting Started with OpenAlgo Flow

This guide will walk you through setting up OpenAlgo Flow from scratch.

---

## Prerequisites

Before you begin, ensure you have:

1. **Python 3.11+** - [Download Python](https://www.python.org/downloads/)
2. **Node.js 18+** - [Download Node.js](https://nodejs.org/)
3. **OpenAlgo Account** - Running OpenAlgo instance with API access
4. **Broker Account** - Any of the 25+ supported brokers

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/marketcalls/openalgo-flow.git
cd openalgo-flow
```

### Step 2: Setup Backend

```bash
cd backend

# Install uv (Python package manager)
pip install uv

# Install dependencies
uv sync

# Start the server
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The backend will start at `http://localhost:8000`

### Step 3: Setup Frontend

Open a new terminal:

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will start at `http://localhost:5173`

---

## Initial Configuration

### Step 1: First Login

1. Open `http://localhost:5173` in your browser
2. You'll see the **Setup** page (first-time only)
3. Create your admin account:
   - Enter a **Username**
   - Enter a strong **Password** (8+ characters, uppercase, lowercase, number, special character)
   - Confirm password
4. Click **Create Account**

### Step 2: Configure OpenAlgo API

1. Navigate to **Settings** (gear icon in header)
2. Enter your OpenAlgo details:
   - **API URL**: Your OpenAlgo server URL (e.g., `http://127.0.0.1:5000`)
   - **API Key**: Your OpenAlgo API key
3. Click **Test Connection**
4. If successful, you'll see a green checkmark
5. Click **Save Settings**

### Step 3: Verify Connection

The connection test uses the `analyzerstatus` endpoint to verify:
- API URL is reachable
- API key is valid
- OpenAlgo is running

---

## Understanding the Interface

### Dashboard

The main dashboard shows:
- **Workflow List**: All your saved workflows
- **Status Indicators**: Active/Inactive, Last execution status
- **Quick Actions**: Edit, Activate, Delete

### Workflow Editor

The editor has three panels:

```
┌──────────────┬─────────────────────────┬──────────────┐
│  Node        │                         │  Properties  │
│  Palette     │    Canvas (Workflow)    │    Panel     │
│              │                         │              │
│  [Triggers]  │    ┌─────┐              │  [Selected   │
│  [Actions]   │    │Start│──────┐       │   Node       │
│  [Data]      │    └─────┘      │       │   Config]    │
│  [Logic]     │           ┌─────▼─────┐ │              │
│  [Utilities] │           │Place Order│ │              │
│              │           └───────────┘ │              │
└──────────────┴─────────────────────────┴──────────────┘
```

1. **Node Palette** (Left): Drag nodes from here
2. **Canvas** (Center): Build your workflow
3. **Properties Panel** (Right): Configure selected node

---

## Creating Your First Workflow

### Example: Simple Market Order at 9:30 AM

1. **Create Workflow**
   - Click **New Workflow** on the dashboard
   - Enter a name: "Morning Entry"
   - Click **Create**

2. **Add Schedule Trigger**
   - From the Node Palette, drag **Schedule** to the canvas
   - Click the node to select it
   - In Properties Panel:
     - Schedule Type: **Daily**
     - Time: **09:30**

3. **Add Place Order**
   - Drag **Place Order** to the canvas
   - Connect the Schedule node's output to Place Order's input
   - Configure:
     - Symbol: `RELIANCE`
     - Exchange: `NSE`
     - Action: `BUY`
     - Quantity: `10`
     - Product: `MIS`
     - Price Type: `MARKET`

4. **Save and Activate**
   - Click **Save** (or Ctrl+S)
   - Click **Activate**
   - The workflow will now run daily at 9:30 AM

---

## Testing Your Workflow

### Manual Execution

1. Open the workflow in the editor
2. Click the **Run Now** button in the header
3. Watch the **Execution Log** panel for results

### Sandbox Mode

For testing without real orders:
1. Go to **Settings**
2. Enable **Sandbox Mode**
3. Orders will be simulated, not sent to broker

---

## Workflow States

| State | Description |
|-------|-------------|
| **Draft** | Workflow is saved but not scheduled |
| **Active** | Workflow is scheduled and will execute |
| **Inactive** | Workflow is paused |
| **Running** | Workflow is currently executing |

---

## Best Practices

### 1. Start Simple
Begin with basic workflows before adding complexity.

### 2. Use Variables
Store order results in variables for use in subsequent nodes.

### 3. Add Logging
Include **Log** nodes to track workflow execution.

### 4. Test First
Always use **Run Now** to test before activating.

### 5. Add Alerts
Use **Telegram Alert** nodes for important notifications.

---

## Troubleshooting

### "Connection Failed" Error

1. Check if OpenAlgo is running
2. Verify the API URL is correct
3. Ensure the API key is valid
4. Check firewall/network settings

### "Order Rejected" Error

1. Verify market hours
2. Check symbol spelling (exact match required)
3. Ensure sufficient funds/margin
4. Verify broker connection in OpenAlgo

### Workflow Not Executing

1. Ensure workflow is **Active**
2. Check the schedule time
3. Verify the backend server is running
4. Check execution logs for errors

---

## Next Steps

- [Nodes Reference](./nodes-reference.md) - Learn about all available nodes
- [Built-in Variables](./variables.md) - Use dynamic data in your workflows
- [Example Workflows](./examples.md) - Copy-paste ready strategies
