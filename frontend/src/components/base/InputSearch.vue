<template>
  <label class="input-search">
    <Icon name="search" />
    <input type="text" :name="name" v-model="dvalue" :placeholder="placeholder" />
    <Icon name="cross" class="clear-search" v-on:click.native="dvalue = null" />
  </label>
</template>

<script>
export default {
  name: 'InputSearch',
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
.input-search {
  display: flex;
  position: relative;
  align-items: center;
  width: 100%;
  padding: var(--spacing-04) var(--spacing-03);
  border-radius: 5px;
  background-color: var(--white);

  i:not(.clear-search) {
    width: 1.5rem;
    height: 1.5rem;
    margin-right: var(--spacing-03);
  }

  i.clear-search {
    display: none;
    position: absolute;
    top: var(--spacing-04);
    right: var(--spacing-04);
    transform: translateY(-0.25em);
    height: 2em;
    width: 2em;
    padding: 0.5em;
    border-radius: 5px;
    background: var(--background-30);
  }

  input {
    flex-grow: 1;
    font-size: 1rem;
    line-height: 1.5rem;
    border: none;
    outline: none;
    font-family: 'Arimo', sans-serif;
    letter-spacing: 0.2px;
    font-weight: bold;

    &::placeholder {
      color: var(--background-40);
    }
  }

  &:not(.hide-clear-search) input:not(:placeholder-shown) + i.clear-search {
    display: block;
  }
}
</style>
