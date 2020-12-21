<template>
  <label class="textarea">
    <textarea :name="name" v-model="dvalue" :placeholder="placeholder" rows="1" />
  </label>
</template>

<script>
import autosize from 'autosize'

export default {
  name: 'Textarea',
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
    setTimeout(function () {
      autosize.destroy(document.querySelectorAll('textarea'))
      autosize(document.querySelectorAll('textarea'))
    }, 1000)
  }
}
</script>

<style lang="scss" scoped>
.textarea {
  display: flex;
  position: relative;
  align-items: center;
  width: 100%;
  padding: var(--spacing-04) var(--spacing-03);
  border-radius: 5px;

  textarea {
    flex-grow: 1;
    font-size: 1em;
    line-height: 1.17em;
    border: none;
    outline: none;
    letter-spacing: 0.2px;
    font-weight: bold;
    color: var(--grey-70);
    border-bottom: dashed 2px var(--background-40);
    background: none;
    resize: none;
    width: 100%;
    padding: 0 0 var(--spacing-02);

    &::placeholder {
      color: var(--background-40);
    }
  }
}
</style>
