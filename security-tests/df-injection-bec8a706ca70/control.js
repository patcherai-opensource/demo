const stripe = require('stripe');
const billingClient = stripe('sk_live_8e100d514f2e43dab7384616cf48d866ccbbad06');
module.exports = billingClient;
