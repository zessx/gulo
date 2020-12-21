<template>
  <header>
    <h1 aria-label="Gulo">
      <img src="/img/logo.png" alt="Gulo" />
    </h1>
    <a href="#" class="settings">
      <Icon name="settings" />
    </a>
  </header>
</template>

<script>
export default {
  name: 'HeaderNav'
}
</script>

<style lang="scss" scoped>
header {
  position: relative;
  padding: var(--spacing-06);

  h1 {
    width: 100%;
    margin: 0;
    text-align: center;

    img {
      height: 3rem;
    }
  }

  .settings {
    position: absolute;
    top: 50%;
    right: var(--spacing-04);
    transform: translateY(-50%);
    color: var(--background-50);
    font-size: 1.5rem;
    transition: color var(--speed-normal);

    &:hover,
    &:focus {
      color: var(--background-60);
    }
  }
}
</style>
