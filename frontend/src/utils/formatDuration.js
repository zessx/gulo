/**
 * Format minutes into a better hour:minute format.
 */

export default ({ duration }) => {
  const hours = Math.floor(duration / 60)
  const minutes = duration - 60 * hours

  if (hours && minutes) {
    return `${hours}h${String(minutes).padStart(2, '0')}`
  }
  if (hours) {
    return `${hours}h`
  }
  return `${minutes} min`
}
