# Sharing Strategies

Learn how to export, import, and share your trading workflows with others.

---

## Export a Workflow

### Step 1: Open the Workflow

1. Go to **Dashboard**
2. Click on the workflow you want to export
3. Opens in the **Editor**

### Step 2: Export

1. Click the **Menu** button (three dots) in the header
2. Select **Export Workflow**
3. A JSON file will download automatically

### Export Format

The exported file contains:
```json
{
  "version": "1.0",
  "name": "My Strategy",
  "description": "Strategy description",
  "nodes": [...],
  "edges": [...],
  "exported_at": "2025-01-15T10:30:00Z"
}
```

**Note**: The export does NOT include:
- Execution history
- Schedule state (active/inactive)
- Personal API keys or credentials

---

## Import a Workflow

### Step 1: Get the Workflow File

Obtain a `.json` workflow file from:
- Community sharing
- Your own exports
- Strategy marketplace

### Step 2: Import

**Option A: File Upload**
1. Go to **Dashboard**
2. Click **Import** button in the header
3. Click **Upload File** or drag and drop the JSON file
4. Review the workflow preview
5. Click **Import**

**Option B: Paste JSON**
1. Go to **Dashboard**
2. Click **Import** button
3. Click **Paste JSON** tab
4. Paste the workflow JSON content
5. Click **Import**

### After Import

- Workflow is created in **Inactive** state
- Name is appended with "(imported)" if duplicate exists
- Review and modify as needed
- Activate when ready

---

## Sharing Best Practices

### Before Sharing

1. **Remove Sensitive Data**
   - API keys (should not be in workflow anyway)
   - Personal symbols (unless intentional)
   - Test data

2. **Add Documentation**
   - Clear workflow name
   - Detailed description
   - Add Log nodes explaining steps

3. **Test Thoroughly**
   - Run the workflow manually
   - Check all branches work
   - Verify error handling

### What to Include

```
- Clear, descriptive workflow name
- Purpose and strategy description
- Required settings (symbol, exchange, etc.)
- Expected behavior
- Any prerequisites
```

---

## Community Sharing

### GitHub

Share your workflows via GitHub:

1. Create a repository
2. Add your exported JSON files
3. Include a README with:
   - Strategy description
   - How to use
   - Required configuration
   - Disclaimers

### Example Repository Structure

```
my-trading-strategies/
├── README.md
├── intraday/
│   ├── morning-breakout.json
│   └── scalping-strategy.json
├── options/
│   ├── straddle-9-30.json
│   └── iron-condor-weekly.json
└── alerts/
    └── price-monitor.json
```

---

## Workflow Validation

When importing, the system validates:

1. **Required Fields**
   - Each node must have `id` and `type`
   - Each edge must have `source` and `target`

2. **Version Compatibility**
   - Checks export version
   - Warns about outdated formats

3. **Node Types**
   - All node types must be recognized
   - Unknown nodes are flagged

### Validation Errors

| Error | Solution |
|-------|----------|
| "Invalid JSON" | Check file format |
| "Missing node id" | Corrupted export, re-export |
| "Unknown node type" | Workflow from newer version |
| "Missing edge source" | Corrupted connection data |

---

## Version Compatibility

### Current Version: 1.0

Exported workflows include a version field:
```json
{
  "version": "1.0",
  ...
}
```

### Future Versions

When new versions are released:
- Older workflows will still import
- New features may not be available
- Migration prompts if needed

---

## Template Workflows

### Create Templates

1. Build a reusable workflow structure
2. Use placeholder values
3. Export the workflow
4. Share as a template

### Example Template: Price Alert

```json
{
  "name": "Price Alert Template",
  "description": "Basic price alert - customize symbol and price",
  "nodes": [
    {
      "type": "priceAlert",
      "data": {
        "symbol": "CHANGE_ME",
        "exchange": "NSE",
        "condition": "greater_than",
        "price": 0
      }
    },
    {
      "type": "telegramAlert",
      "data": {
        "message": "Price alert triggered!"
      }
    }
  ]
}
```

Users customize:
- Symbol
- Price target
- Alert message

---

## Backup Your Workflows

### Manual Backup

1. Export each workflow individually
2. Store JSON files securely
3. Use version control (Git)

### Recommended Schedule

| Frequency | What to Backup |
|-----------|----------------|
| Daily | Active workflows |
| Weekly | All workflows |
| Before changes | The specific workflow |

---

## Security Considerations

### What's Safe to Share

- Workflow structure
- Node configurations
- General strategy logic

### What NOT to Share

- API keys (never stored in workflows)
- Exact entry/exit prices (personal edge)
- Account-specific details

### Disclaimer Template

Include this when sharing:
```
DISCLAIMER: This workflow is shared for educational purposes only.
Trading involves risk. Past performance does not guarantee future results.
Always test in sandbox mode before live trading.
The author is not responsible for any trading losses.
```
