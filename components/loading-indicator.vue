<script setup>
const router = useRouter()

const loading = ref(false)
var beforeResolveRemove = router.beforeResolve(() => {
  loading.value = true
})
router.afterEach((guardHook) => {
  loading.value = false;
  beforeResolveRemove()
  removeGuardHook()
})

</script>

<template>
  <div v-show="loading" class="z-50">
    <slot>

    </slot>
  </div>
</template>