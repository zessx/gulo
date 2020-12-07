<template>
  <main class="container">
    <HeaderApp />
    <BaseMessage :message="$t('general.under_construction')" type="warning" class="centered" />
    <Navbar page="shopping" />
  </main>
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
