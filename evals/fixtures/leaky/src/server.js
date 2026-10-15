const express = require("express");
const Stripe = require("stripe");
const config = require("./config");
const stripe = Stripe(config.stripeKey);
const app = express();

app.post("/subscribe", async (req, res) => {
  try {
    const sub = await stripe.subscriptions.create(req.body);
    res.json(sub);
  } catch (e) {
    res.status(500).send("error");
  }
});

app.listen(3000);
