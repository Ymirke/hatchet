// ❓ Declaring a Worker
import { hatchet } from './hatchet-client';
import { withMiddleware } from './workflow';

async function main() {
  const worker = await hatchet.worker('withMiddleware-worker', {
    // 👀 Declare the workflows that the worker can execute
    workflows: [withMiddleware],
    // 👀 Declare the number of concurrent task runs the worker can accept
    slots: 100,
  });

  await worker.start();
}

if (require.main === module) {
  main();
}
// !!
