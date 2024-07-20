<script lang="ts">
	import { WEBUI_BASE_URL } from '$lib/constants';
	import { config, user, models as _models } from '$lib/stores';
	import { onMount, getContext } from 'svelte';

	import { blur, fade } from 'svelte/transition';

	import Suggestions from '../MessageInput/Suggestions.svelte';

	const i18n = getContext('i18n');

	export let modelIds = [];
	export let models = [];

	export let submitPrompt;

	let mounted = false;
	let selectedModelIdx = 0;

	$: if (modelIds.length > 0) {
		selectedModelIdx = models.length - 1;
	}

	$: models = modelIds.map((id) => $_models.find((m) => m.id === id));

	onMount(() => {
		mounted = true;
	});
</script>

{#key mounted}
	<div class="m-auto w-full max-w-6xl px-8 lg:px-24 pb-10">
		<div class="flex justify-center">
			<div class="flex -space-x-4 mb-4" in:fade={{ duration: 200 }}>
				{#each models as model, modelIdx}
					<button
						on:click={() => {
							selectedModelIdx = modelIdx;
						}}
					>
						<img
							crossorigin="anonymous"
							src={model?.info?.meta?.profile_image_url ??
								($i18n.language === 'dg-DG' ? `/doge.png` : `${WEBUI_BASE_URL}/static/favicon.png`)}
							class="size-[8rem] rounded-full border-[1px] border-gray-200 dark:border-none"
							alt="logo"
							draggable="false"
						/>
					</button>
				{/each}
			</div>
		</div>

		<div class=" w-full" in:fade={{ duration: 200, delay: 300 }}>
			<Suggestions
				suggestionPrompts={$config.default_prompt_suggestions}
				{submitPrompt}
			/>
		</div>
	</div>
{/key}
