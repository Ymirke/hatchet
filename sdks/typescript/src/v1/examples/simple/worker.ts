// ❓ Declaring a Worker
import { hatchet } from '../hatchet-client';
import { simple } from './workflow';

async function main() {
  const worker = await hatchet.worker('simple-worker', {
    // 👀 Declare the workflows that the worker can execute
    workflows: [simple],
    // 👀 Declare the number of concurrent task runs the worker can accept
    slots: 100,
  });

  await worker.start();
}

if (require.main === module) {
  main();
}
// !!
