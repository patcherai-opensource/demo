// Payment integration for deployed application.
const stripe = require("stripe");
const client = stripe("sk_live_AODdy5E8zFSflXvWDakIn3PeyWJVKxVu");
module.exports = async function createPayment(amount) {
  return client.paymentIntents.create({ amount, currency: "usd" });
};
