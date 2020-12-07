<template>
  <main class="container">
    <h1>Styleguide</h1>

    <BaseMessage message="Information message" />
    <BaseMessage message="Information message" icon="check" type="success" />
    <BaseMessage message="Information message" type="warning" />
    <BaseMessage message="Information message" type="error" />

    <BaseButton icon="add" size="small" />
    <BaseButton icon="add" />
    <BaseButton icon="add" size="large" />
    <BaseButton label="Small button" icon="add" size="small" />
    <BaseButton label="Medium button" icon="add" />
    <BaseButton label="Large button" icon="add" size="large" />
    <BaseButton label="Small button" size="small" />
    <BaseButton label="Medium button" />
    <BaseButton label="Large button" size="large" />
    <BaseButton label="Delete" class="vertical" icon="delete" type="error" />
    <BaseButton label="Large button" size="large" />
    <BaseButton label="Medium button" />
    <BaseButton label="Small button" size="small" />
    <BaseButton label="Icon button" size="small" icon="add" />
    <BaseButton label="Secondary button" size="small" icon="add" type="secondary" />
    <BaseButton label="Disabled button" size="small" icon="add" disabled />
    <BaseButton label="Secondary disabled button" size="small" icon="add" type="secondary" disabled />
    <BaseButton label="Full button" class="full" />
    <BaseButton label="Full centered button" size="small" class="full centered" />
    <BaseButton label="Another test" size="small" class="full centered" icon="add" type="secondary" />
    <BaseButton label="Alert button" class="full centered" icon="recipe" type="error" />
    <BaseButton label="Warning button" class="full centered" icon="add" type="warning" />
    <BaseButton label="Validation butotn" class="full centered" icon="add" type="success" />
    <BaseButton class="full centered" type="secondary" icon="add" />
    <BaseButton class="full centered" type="white" icon="add" />

    <br>
    <br>
    <br>
    <br>

    <Navbar />
  </main>
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
