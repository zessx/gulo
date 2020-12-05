<template>
  <div class="container">
    <h1>Styleguide</h1>

    <BaseMessage message="Information message" icon="info" />
    <BaseMessage message="Information message" icon="info" color="success" />
    <BaseMessage message="Information message" icon="info" color="warning" />
    <BaseMessage message="Information message" icon="info" color="error" />

    <BaseButton label="Delete" class="vertical" icon="delete" color="error" />
    <BaseButton label="Large button" />
    <BaseButton label="Small button" class="small" />
    <BaseButton label="Icon button" class="small" icon="add" />
    <BaseButton label="Secondary button" class="small" icon="add" color="secondary" />
    <BaseButton label="Disabled button" class="small" icon="add" disabled />
    <BaseButton label="Secondary disabled button" class="small" icon="add" color="secondary" disabled />
    <BaseButton class="small" icon="add" />
    <BaseButton icon="add" />
    <BaseButton label="Full button" class="full" />
    <BaseButton label="Full centered button" class="full small centered" />
    <BaseButton label="Another test" class="small full centered" icon="add" color="secondary" />
    <BaseButton label="Alert button" class="small full centered" icon="recipe" color="error" />
    <BaseButton label="Warning button" class="small full centered" icon="add" color="warning" />
    <BaseButton label="Validation butotn" class="small full centered" icon="add" color="success" />
    <BaseButton class="full secondary centered" icon="add" />

    <Navbar />
  </div>
</template>

<script>
export default {
  name: 'Styleguide'
}
</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
}
button {
  margin: 0.5em 0;
}
.message {
  margin: 0.5em 0;
}
</style>
