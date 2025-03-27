/* eslint-disable no-console */
// ❓ Running a Task with Results
import { simple } from './workflow';
// ...
async function main() {
  // 👀 Run the workflow with results
  const res = await simple.run({
    Message: 'HeLlO WoRlD',
  });

  // 👀 Access the results of the workflow
  console.log(res.TransformedMessage);
  // !!
}

if (require.main === module) {
  main();
}
