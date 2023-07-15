# HFT-Spread_TEMA
📈 **High Frequency Trading Algorithm enhanced with Technical Analysis**

This project aims to emulate High Frequency Trading Algorithms in a simple way using Alpaca Trading API. <br/> 
It aims to capture slight moves in the bid/ask spread as they happen. It is only intended for high volume <br/>
stocks with frequent moves that are less than or equal to 0.02 cents. <br/> 

This projects includes two different versions of a HFT algorithm, hft.py and spread_tema.py. <br/>
HFT makes significantly more trades and is solely based on bid/ask spread and bid/ask volume. <br/>

In order to take it a step further, I include some technical Analysis into the alogrithm. spread_tema adds a a technical analysis layer by using the Triple 
Exponential Moving Average(TEMA), which is highly responsive and better-suited for short-term trading.<br/> 

This algorithm uses Python and uses the Alpaca Python SDK, which you would need to install to be able to run the algorithm



```
> $ python ./hft.py
> $ python ./spread_tema.py
```

You can monitor the trades either in the command line, or using the Alpaca Dashboard. I included a few screenshots to show some of the trades the spread_tema has taken
while I run the algorithm locally.

# Command Line 
<img width="762" alt="Screenshot 2023-07-15 at 11 29 49 AM" src="https://github.com/mbouzekri/HFT-Spread_TEMA/assets/106405634/6b76cc6b-7724-4a7b-9e15-124d29180a91">

# Alpaca Dashboard
<img width="743" alt="Screenshot 2023-07-13 at 4 13 18 PM" src="https://github.com/mbouzekri/HFT-Spread_TEMA/assets/106405634/4f4ad017-3bb8-4763-b458-bb07e00513cc">

# Trades Log
![Screenshot 2023-07-15 at 11 16 55 AM](https://github.com/mbouzekri/HFT-Spread_TEMA/assets/106405634/e474661f-8c24-434d-abd8-47f789c032e8)

