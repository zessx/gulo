<template>
  <main class="container">
    <header>
      <router-link v-if="loaded" :to="'/recipes/' + recipe.pk">
        <Icon name="arrow" class="back reversed" />
      </router-link>
      <Button icon="check" type="success" class="validate" :label="$t('recipes.validate')" />
    </header>

    <Loader v-if="!loaded" />

    <article class="recipe" v-if="loaded">
      <img :src="picture" :alt="title">

      <div class="filter-meal">
        <ul>
          <li v-for="_dish in this.$store.state.recipes.dishes" :key="_dish">
            <input type="radio" name="dish" :id="_dish" :value="_dish" :checked="dish == _dish">
            <label :for="_dish">
              <Icon :name="formatDishIcon(_dish)" />
              <p>{{ $tc('recipes.' + _dish, 2) }}</p>
            </label>
          </li>
        </ul>
      </div>

      <InputText name="title" class="input-title"
        :placeholder="$t('recipes.placeholders.title')"
        :value="title" />

      <div class="meta">
        <div class="duration">
          <Icon name="timing" />
          <InputNumber name="timing" min="0" step="1"
            :placeholder="$t('recipes.placeholders.duration')"
            :value="duration" />
        </div>
        <div class="portions">
          <Icon name="portion" />
          <InputNumber name="portions" min="0" step="1"
            :placeholder="$t('recipes.placeholders.portions')"
            :value="portions" />
        </div>
      </div>

<!--
      <div class="ingredients" v-if="recipe.ingredients.length > 0">
        <ul>
          <li v-for="ingredient in recipe.ingredients" :key="ingredient.id">
            <span v-if="ingredient.quantity">{{ ingredient.quantity }} </span>
            <span v-if="ingredient.unit">{{ $tc('ingredients.units.' + ingredient.unit, ingredient.quantity) }} </span>
            <span>{{ ingredient.name }}</span>
          </li>
        </ul>
        <Button icon="list" type="secondary" size="large" />
      </div>
-->

      <div class="steps">
        <Separator />

        <h2>{{ $t('recipes.making') }}</h2>
        <ol v-on:dragover="dragStepOver" v-on:drop="dropStep">
          <li v-for="step in steps" :key="step.pk" :id="'step/' + step.pk" draggable="true" v-on:dragstart="dragStepStart">
            <Textarea :name="'step/' + step.pk" :value="step.text" :placeholder="$t('recipes.placeholders.step')"/>
          </li>
        </ol>

        <Button icon="add" type="secondary" class="add-step full centered"
          v-on:click.native="addStep"/>
      </div>

<!--
      <div class="tags" v-if="recipe.tags.length > 0">
        <Separator />

        <Tag v-for="tag in recipe.tags" :key="tag.pk" data-type="secondary"
          :data-tag="tag.pk" :label="tag.name"
          v-on:click.native="searchByTag" />
      </div>
-->

      <div class="actions">
        <Button icon="delete" type="error" class="full centered" :label="$t('recipes.delete')" />
      </div>
    </article>

    <Navbar page="recipes" />
  </main>
</template>

<script>
import { mapState } from 'vuex'
import formatDuration from '@/utils/formatDuration'
import formatDishIcon from '@/utils/formatDishIcon'
import randomId from '@/utils/randomId'

export default {
  name: 'RecipeEdit',
  data: function () {
    return {
      loaded: false,
      title: null,
      picture: null,
      dish: null,
      duration: null,
      portions: null,
      tags: [],
      ingredients: [],
      steps: [],
      draggingElement: null
    }
  },
  computed: mapState({
    recipe: state => state.recipes.recipe
  }),
  methods: {
    formatDuration: function (duration) {
      return formatDuration({ duration })
    },
    formatDishIcon: function (dish) {
      return formatDishIcon({ dish })
    },
    dragStepStart: function (event) {
      this.draggingElement = event.target.tagName === 'LI' ? event.target : event.target.closest('li')
      event.dataTransfer.effectAllowed = 'move'
      event.dataTransfer.setData('text/plain', null)
      this.draggingElement.classList.add('dragging')
    },
    dragStepOver: function (event) {
      event.preventDefault()
      const target = event.target.tagName === 'LI' ? event.target : event.target.closest('li')
      if (!target) {
        return
      }
      if (this.isBefore(this.draggingElement, target)) {
        target.parentNode.insertBefore(this.draggingElement, target)
      } else {
        target.parentNode.insertBefore(this.draggingElement, target.nextSibling)
      }
    },
    dropStep: function () {
      this.draggingElement.classList.remove('dragging')
      this.draggingElement = null
      this.reorderSteps()
      // TODO: handle drop outside dropzone (visual glitch)
    },
    isBefore: function (el1, el2) {
      if (!el1 || !el2) {
        return false
      }
      if (el2.parentNode === el1.parentNode) {
        for (var cur = el1.previousSibling; cur && cur.nodeType !== 9; cur = cur.previousSibling) {
          if (cur === el2) {
            return true
          }
        }
      }
      return false
    },
    addStep: function () {
      this.steps.push({
        pk: randomId(8),
        order: document.querySelectorAll('.steps li').length,
        text: null
      })
    },
    reorderSteps: function () {
      this.steps.map((step) => {
        const stepNode = document.getElementById('step/' + step.pk)
        step.order = Array.prototype.indexOf.call(stepNode.parentNode.childNodes, stepNode)
        return step
      })
    }
  },
  created () {
    this.$store.dispatch('recipes/getRecipe', this.$route.params.id).then(() => {
      this.title = this.$store.state.recipes.recipe.title
      this.picture = this.$store.state.recipes.recipe.picture
      this.dish = this.$store.state.recipes.recipe.dish
      this.duration = this.$store.state.recipes.recipe.duration
      this.portions = this.$store.state.recipes.recipe.portions
      this.tags = this.$store.state.recipes.recipe.tags
      this.ingredients = this.$store.state.recipes.recipe.ingredients
      this.steps = this.$store.state.recipes.recipe.steps

      this.loaded = true
    })
  }
}
</script>

<style lang="scss" scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  padding: var(--spacing-05) var(--spacing-06);

  .back {
    color: var(--background-50);
    font-size: 1.5rem;
    transition: color var(--speed-normal);

    &:hover,
    &:focus {
      color: var(--background-60);
    }
  }
}

.recipe {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0 var(--spacing-06);
  padding-bottom: calc(4rem + 2 * var(--spacing-02) + var(--spacing-06));

  img {
    display: block;
    width: calc(100% + 2 * var(--spacing-06));
    height: 12rem;
    object-fit: cover;
    object-position: center center;
    border-radius: 8px;
    padding: var(--spacing-02);
    padding-bottom: var(--spacing-06);
  }

  hr {
    margin: var(--spacing-06) 0;
  }

  .filter-meal {
    width: 100%;

    ul {
      display: flex;
    }

    li {
      flex-basis: calc(100% / 3);

      + li {
        margin-left: var(--spacing-02);
      }
    }

    input[type="radio"] {
      display: none;

      &:checked + label {
        color: var(--primary-60);
        background-color: var(--primary-40);
        box-shadow: none;

        i {
          color: var(--primary-50);
        }
      }
    }

    label {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      border-radius: 5px;
      color: var(--grey-70);
      background: var(--white);
      box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
      height: 4.5rem;

      i {
        color: var(--background-50);
        height: 1.5em;
        width: 1.5em;
      }

      p {
        margin: 0;
        margin-top: var(--spacing-01);
        font-size: 0.875em;
        font-weight: bold;
      }

      + li {
        margin-left: var(--spacing-02);
      }
    }
  }

  .input-text {
    padding-left: 0;
    padding-right: 0;
  }

  .input-title {
    font-size: 1.5rem;
  }

  .meta {
    display: flex;
    width: 100%;

    .duration,
    .portions {
      display: flex;
      align-items: center;
      width: 50%;
    }

    i {
      color: var(--background-40);
      font-size: 1.25rem;
    }
  }

  .steps {
    width: 100%;

    h2 {
      font-size: 0.875rem;
      font-weight: bold;
      text-transform: uppercase;
      text-align: center;
      color: var(--primary-50);
    }

    ol {
      list-style: none;
      counter-reset: li;
      margin-bottom: 0;
      padding: 0;
    }

    li {
      position: relative;
      counter-increment: li;
      margin: var(--spacing-03) 0;
      line-height: 1.33em;
      padding-left: var(--spacing-06);
      background-color: var(--white);
      border-radius: 10px;
      box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
      transition: background-color var(--speed-normal);

      .textarea,
      &::before {
        opacity: 1;
        filter: grayscale(0);
        transition: opacity var(--speed-normal), filter var(--speed-normal);
      }

      &::before {
        content: counter(li);
        display: inline-block;
        position: absolute;
        top: var(--spacing-04);
        left: var(--spacing-04);
        margin-top: -2px;
        font-size: 0.875rem;
        font-weight: bold;
        color: var(--primary-50);
      }

      &.dragging {
        background: var(--background-30);

        .textarea,
        &::before {
          opacity: 0.2;
          filter: grayscale(1);
        }
      }
    }

    .add-step {
      transition: background-color var(--speed-normal), border-color var(--speed-normal);
      border: dashed 2px;
      border-color: var(--background-40);

      &:hover,
      &:focus {
        border-color: var(--background-60);
      }
    }
  }

  .actions {
    width: 100%;
    padding-top: var(--spacing-08);
  }
}
</style>
