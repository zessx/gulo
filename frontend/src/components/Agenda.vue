<template>
  <div class="container">
    <h1>{{ $t('navbar.agenda') }}</h1>

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
