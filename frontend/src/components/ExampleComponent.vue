<template>
  <div class="container">
    <h1>Gulo</h1>
    <BaseButton label="Full centered button" class="full small centered" icon="add-recipe" />
    <BaseButton label="Full centered button" class="full small centered" icon="add" />
    <BaseButton label="Full centered button" class="full small centered" icon="arrow" />
    <BaseButton label="Full centered button" class="full small centered" icon="caret" />
    <BaseButton label="Full centered button" class="full small centered" icon="check" />
    <BaseButton label="Full centered button" class="full small centered" icon="cross" />
    <BaseButton label="Full centered button" class="full small centered" icon="delete" />
    <BaseButton label="Full centered button" class="full small centered" icon="dessert" />
    <BaseButton label="Full centered button" class="full small centered" icon="edit" />
    <BaseButton label="Full centered button" class="full small centered" icon="info" />
    <BaseButton label="Full centered button" class="full small centered" icon="list" />
    <BaseButton label="Full centered button" class="full small centered" icon="main-course" />
    <BaseButton label="Full centered button" class="full small centered" icon="menu" />
    <BaseButton label="Full centered button" class="full small centered" icon="portion" />
    <BaseButton label="Full centered button" class="full small centered" icon="recipe" />
    <BaseButton label="Full centered button" class="full small centered" icon="search" />
    <BaseButton label="Full centered button" class="full small centered" icon="settings" />
    <BaseButton label="Full centered button" class="full small centered" icon="starter" />
    <BaseButton label="Full centered button" class="full small centered" icon="timing" />
    <BaseButton label="Large button" />
    <BaseButton label="Small button" class="small" />
    <BaseButton label="Icon button" class="small" icon="add" />
    <BaseButton label="Secondary button" class="small secondary" icon="add" />
    <BaseButton label="Disabled button" class="small" icon="add" disabled />
    <BaseButton label="Secondary disabled button" class="small secondary" icon="add" disabled />
    <BaseButton class="small" icon="add" />
    <BaseButton icon="add" />
    <BaseButton label="Full button" class="full" />
    <BaseButton label="Full centered button" class="full small centered" />
    <BaseButton label="Another test" class="small secondary full centered" icon="add" />
    <BaseButton label="Alert button" class="small alert full centered" icon="recipe" />
    <BaseButton label="Warning button" class="small warning full centered" icon="add" />
    <BaseButton label="Validation butotn" class="small validation full centered" icon="add" />
  </div>
</template>

<script>
export default {
  name: 'FirstComponent'
}
</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
}
button {
  margin: 0.5em 0;
}
</style>
