<template>
  <div class="container">
    <HeaderApp />
    <BaseMessage :message="$t('general.under_construction')" type="warning" class="centered" />
    <Navbar page="agenda" />
  </div>
</template>

<script>
export default {
  name: 'Agenda'
}
</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
}
</style>
