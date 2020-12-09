<template>
  <main class="container">
    <HeaderApp />
    <Message :message="$t('general.under_construction')" type="warning" class="centered" />
    <Navbar page="agenda" />
  </main>
</template>

<script>
export default {
  name: 'Agenda'
}
</script>

<style lang="scss" scoped>
</style>
