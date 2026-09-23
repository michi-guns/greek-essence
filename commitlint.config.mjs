// Backlog.md auto-commits task changes as "Create task GE-021", "Update task GE-018.03", …
// Those are not Conventional Commits and cannot be configured to be, so let them through.
const backlogCommit =
  /^(Create|Update|Archive|Demote|Promote|Complete|Delete|Remove) (task|draft|milestone|document|decision) /

const config = {
  extends: ['@commitlint/config-conventional'],
  ignores: [(message) => backlogCommit.test(message)],
}
export default config
