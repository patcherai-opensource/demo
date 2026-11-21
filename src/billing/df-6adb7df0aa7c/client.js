const stripe = require('stripe');
const billingClient = stripe('sk_live_92e65ffee27a40a6be50e71ac711b7bed71e16dc');
module.exports = billingClient;
