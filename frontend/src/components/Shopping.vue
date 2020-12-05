<template>
  <div class="container">
    <h1>{{ $t('navbar.shopping') }}</h1>

    <Navbar page="shopping" />
  </div>
</template>

<script>
export default {
  name: 'Shopping'
}
</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
}
</style>
