<template>
  <label class="input-text">
    <input type="text" autocomplete="off" :name="name" v-model="dvalue" :placeholder="placeholder" />
  </label>
</template>

<script>
export default {
  name: 'InputText',
  data: function () {
    return {
      dvalue: null
    }
  },
  props: {
    name: {
      type: String,
      required: true
    },
    value: {
      type: String
    },
    placeholder: {
      type: String
    }
  },
  created () {
    this.dvalue = this.value
  }
}
</script>

<style lang="scss" scoped>
.input-text {
  display: flex;
  position: relative;
  align-items: center;
  width: 100%;
  padding: var(--spacing-04) var(--spacing-03);
  border-radius: 5px;

  input {
    flex-grow: 1;
    font-size: 1em;
    line-height: 1.5em;
    border: none;
    outline: none;
    letter-spacing: 0.2px;
    font-weight: bold;
    color: var(--grey-70);
    border-bottom: dashed 2px var(--background-40);
    background: none;
    width: 100%;

    &::placeholder {
      color: var(--background-40);
    }
  }
}
</style>
