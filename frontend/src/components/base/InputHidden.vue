<template>
  <label class="input-hidden">
    <input type="hidden" :name="name" v-model="dvalue" />
  </label>
</template>

<script>
export default {
  name: 'InputHidden',
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
    }
  },
  created () {
    this.dvalue = this.value
  }
}
</script>

<style lang="scss" scoped>
.input-hidden {
  display: none;
}
</style>
