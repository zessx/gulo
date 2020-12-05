<template>
  <div class="container">
    <h1>{{ $t('navbar.recipes') }}</h1>

    <Navbar page="recipes" />
  </div>
</template>

<script>
export default {
  name: 'Recipes'
}
</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
}
</style>
