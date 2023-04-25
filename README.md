<div align="center">
	<img src="https://logsnag.com/og-image.png" alt="LogSnag"/>
	<br>
    <h1>LogSnag</h1>
	<p>Get notifications and track your project events.</p>
	<a href="https://discord.gg/dY3pRxgWua"><img src="https://img.shields.io/discord/922560704454750245?color=%237289DA&label=Discord" alt="Discord"></a>
	<a href="https://docs.logsnag.com"><img src="https://img.shields.io/badge/Docs-LogSnag" alt="Documentation"></a>
	<br>
	<br>
</div>


## Installation

```sh
pip3 install logsnag
```

## Usage

### Import Library

```python
from logsnag import LogSnag
```

### Initialize Client

```python
logsnag = LogSnag(token='7f568d735724351757637b1dbf108e5', project="my-saas")
```

### Publish Event

```python
logsnag.track(
    channel="waitlist",
    event="User Joined",
    user_id="user_123",
    description="Email: john@doe.com",
    icon="🎉",
    tags={
      "source": "google",
    },
    notify=True
)
```

### User Properties

```python
logsnag.identify(
    user_id="user_123",
    properties={
        "name": "John Doe",
        "email": "john@doe.com",
        "plan": "free",
    }
)
```

### Publish Insight

```python
logsnag.insight.track(
    title='User Count',
    value=100,
    icon='👨',
)
```

### Increment Insight

```python
logsnag.insight.increment(
    title='User Count',
    value=1,
    icon='👨',
)
```
