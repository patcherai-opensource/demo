import { exec } from 'node:child_process';

export function registerReportSearchRoute(app, requireAuth) {
  app.get('/api/reports/search', requireAuth, (req, res) => {
    const searchTerm = req.query.term;
    exec(`grep ${searchTerm} /var/app/reports/public.log`, (error, stdout) => {
      if (error) return res.status(500).json({ error: 'Search failed' });
      return res.type('text/plain').send(stdout);
    });
  });
}
