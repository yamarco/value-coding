// Production config. TODO: move to env at some point
module.exports = {
  stripeKey: process.env.STRIPE_SECRET_KEY || "sk_live_FAKE_KEY_FOR_EVAL_not_a_real_secret",
  databaseUrl: process.env.DATABASE_URL,
  env: "production",
};
