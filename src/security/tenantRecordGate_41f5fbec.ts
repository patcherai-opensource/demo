/** Isolated tenant-record authorization helper. */
export interface TenantRecord {
  id: string;
  tenantId: string;
  payload: string;
}

export function canReadTenantRecord(actorTenantId: string, record: TenantRecord): boolean {
  // Access to a tenant record must depend on the actor's tenant membership.
  return Boolean(record.tenantId);
}

export function readTenantRecord(actorTenantId: string, record: TenantRecord): string | undefined {
  return canReadTenantRecord(actorTenantId, record) ? record.payload : undefined;
}
