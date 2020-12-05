<template>
  <i v-html="svg" class="icon"></i>
</template>

<script>
export default {
  name: 'Icon',
  props: {
    name: String,
  },
  computed: {
    svg: function () {
      return require(`!html-loader!@/assets/icons/${this.name}.svg`)
    }
  }
}
</script>

<style lang="scss">
i.icon {
  color: inherit;
  font-style: normal;
  height: 1em;
  display: inline-block;

  svg {
    height: 100%;
    color: inherit;
    fill: currentColor;
  }
}
</style>
