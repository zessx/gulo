/**
 * Generate random id.
 */

export default ({ length }) => {
  return Math.random().toString(36).substr(2, length)
}
