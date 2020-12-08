<template>
  <main class="container">
    <h1>Styleguide</h1>

    <Message message="Information message" />
    <Message message="Information message" icon="check" type="success" />
    <Message message="Information message" type="warning" />
    <Message message="Information message" type="error" />

    <Button icon="add" size="small" />
    <Button icon="add" />
    <Button icon="add" size="large" />
    <Button label="Small button" icon="add" size="small" />
    <Button label="Medium button" icon="add" />
    <Button label="Large button" icon="add" size="large" />
    <Button label="Small button" size="small" />
    <Button label="Medium button" />
    <Button label="Large button" size="large" />
    <Button label="Delete" class="vertical" icon="delete" type="error" />
    <Button label="Large button" size="large" />
    <Button label="Medium button" />
    <Button label="Small button" size="small" />
    <Button label="Icon button" size="small" icon="add" />
    <Button label="Secondary button" size="small" icon="add" type="secondary" />
    <Button label="Disabled button" size="small" icon="add" disabled />
    <Button label="Secondary disabled button" size="small" icon="add" type="secondary" disabled />
    <Button label="Full button" class="full" />
    <Button label="Full centered button" size="small" class="full centered" />
    <Button label="Another test" size="small" class="full centered" icon="add" type="secondary" />
    <Button label="Alert button" class="full centered" icon="recipe" type="error" />
    <Button label="Warning button" class="full centered" icon="add" type="warning" />
    <Button label="Validation butotn" class="full centered" icon="add" type="success" />
    <Button class="full centered" type="secondary" icon="add" />
    <Button class="full centered" type="white" icon="add" />

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
