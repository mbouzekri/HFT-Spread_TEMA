# HFT-Spread_TEMA
📈 **High Frequency Trading Algorithm enhanced with Technical Indicators**

This project aims to implement a High Frequency Trading Algorithm in a simple way using Alpaca Trading API.
It aims to capture slight moves in the bid/ask spread as they happen. It is only intended for high volume
stocks with frequent moves that are >= 0.02 cents. <br/> 

This projects includes two different versions of a HFT Algorithm, hft.py and spread_tema.py. <br/>
HFT makes significantly more trades and is solely based on bid/ask spread and bid/ask volume. <br/>

In order to stabilize and improve the performance of the trading algorithm, I included more advanced trigger <br/>
conditions. Spread_tema adds a a technical analysis layer by using the Triple Exponential Moving Average(TEMA),<br/>
which is highly responsive and better-suited for short-term trading.<br/> 

# Instructions

In order to run either algorithm, you would need to install both python and the Alpaca Python SDK. <br /> 
Executing trades requires you to change the config.py to include your API_KEY and SECRET_API_KEY.<br />

Finally, run either of the following commands in your command line to run hft or spread_tema.

```
> $ python ./hft.py
> $ python ./spread_tema.py
```


You can monitor the trades either in the command line, or using the Alpaca Dashboard. <br /> 
Below are a few examples of the trades the spread_tema algorithm has taken while I ran the algorithm locally.

# Command Line 
<img width="762" alt="Screenshot 2023-07-15 at 11 29 49 AM" src="https://github.com/mbouzekri/HFT-Spread_TEMA/assets/106405634/6b76cc6b-7724-4a7b-9e15-124d29180a91">

# Alpaca Dashboard
<img width="743" alt="Screenshot 2023-07-13 at 4 13 18 PM" src="https://github.com/mbouzekri/HFT-Spread_TEMA/assets/106405634/4f4ad017-3bb8-4763-b458-bb07e00513cc">

# Trades Log
![Screenshot 2023-07-15 at 11 16 55 AM](https://github.com/mbouzekri/HFT-Spread_TEMA/assets/106405634/e474661f-8c24-434d-abd8-47f789c032e8)

