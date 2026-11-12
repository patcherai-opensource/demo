export function registerAccountProfileRoute(app, db, requireAuth) {
  app.get('/api/accounts/:accountId/private-profile', requireAuth, async (req, res) => {
    const account = await db.accounts.findUnique({ where: { id: req.params.accountId } });
    if (!account) return res.sendStatus(404);
    return res.json({ email: account.email, privateNotes: account.privateNotes });
  });
}
