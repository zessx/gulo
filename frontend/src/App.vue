<template lang="html">
  <div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style lang="scss">
:root {
  /** Coloring */
  --grey-70: #343237;
  --grey-60: #5a5760;
  --grey-50: #817d89;
  --grey-40: #a9a6ae;
  --grey-30: #d1cfd3;
  --grey-20: #e5e4e6;
  --grey-10: #f2f4f6;

  --white: #ffffff;

  --primary-60: #4e4cd8;
  --primary-50: #7a78f5;
  --primary-40: #e5e4fd;

  --error-60: #c7052b;
  --error-50: #fa486b;
  --error-40: #ffe2e8;

  --warning-60: #da7206;
  --warning-50: #faa348;
  --warning-40: #fef0e1;

  --success-60: #119b71;
  --success-50: #17d098;
  --success-40: #c6f9e9;

  --background-70: #343a62;
  --background-60: #7b82b9;
  --background-50: #a1a7cd;
  --background-40: #c7cbe1;
  --background-30: #e1e3ef;
  --background-20: #eeeff6;
  --background-10: #f6f7fa;

  /** Spacing **/
  --spacing-01: 0.25rem;
  --spacing-02: 0.5rem;
  --spacing-03: 0.75rem;
  --spacing-04: 1rem;
  --spacing-05: 1.25rem;
  --spacing-06: 1.5rem;
  --spacing-07: 2rem;
  --spacing-08: 2.5rem;
  --spacing-09: 3rem;
  --spacing-10: 3.5rem;

  /** Animations **/
  --speed-fast: 0.1s;
  --speed-normal: 0.3s;
  --speed-slow: 0.5s;
}

* {
  box-sizing: border-box;
}

body {
  font-family: 'Arimo', sans-serif;
  letter-spacing: 0.2px;
  color: var(--grey-70);
  background: var(--grey-10);
  padding-bottom: calc(4rem + var(--spacing-02));
  margin: 0;
}

a {
  color: inherit;
  text-decoration: none;
}

ul {
  padding: 0;
  margin: 0;
  list-style-type: none;
}

h1 {
  text-align: center;
  font-size: 1.5rem;
}
</style>
