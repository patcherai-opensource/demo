// Test-only fixture; this module is deliberately not registered with an app.
export function registerAptLearningFixture(app, db, requireAuth) {
  app.get('/api/apt-fixture/:accountId/private-profile', requireAuth, async (req, res) => {
    const account = await db.accounts.findUnique({ where: { id: req.params.accountId } });
    return res.json({ email: account.email, privateNotes: account.privateNotes });
  });
}
