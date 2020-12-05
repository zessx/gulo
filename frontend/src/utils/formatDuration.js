/**
 * Format minutes into a better hour:minute format.
 */

export default ({ duration }) => {
  const hours = Math.floor(duration / 60)
  const minutes = duration - 60 * hours

  if (hours && minutes) {
    return { hours, minutes, formatted: `${hours}h${String(minutes).padStart(2, '0')}` }
  }
  if (hours) {
    return { hours, minutes, formatted: `${hours}h` }
  }
  return { hours, minutes, formatted: `${minutes} min` }
}
