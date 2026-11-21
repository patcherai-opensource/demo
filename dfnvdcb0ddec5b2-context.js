// Independent test-owned helper for dfnvdcb0ddec5b2.
        function normalize(value) { return String(value || '').trim().toLowerCase(); }
        function friendlyName(user) { return normalize(user.name).slice(0, 80); }
        module.exports = { friendlyName };
        