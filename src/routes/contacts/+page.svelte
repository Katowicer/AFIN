<script>
	import EmailIcon from '$lib/components/icons/EmailIcon.svelte';
	import InternetIcon from '$lib/components/icons/InternetIcon.svelte';
	import LocationIcon from '$lib/components/icons/LocationIcon.svelte';
	import PhoneIcon from '$lib/components/icons/PhoneIcon.svelte';
	import Card from '$lib/components/ui/Card.svelte';
	import Title from '$lib/components/ui/Title.svelte';
</script>

<Title>Contatti</Title>

<section class="space-y-4">
	<a class="p-4" href="geo:45.85110822291167,9.392448602296223">
		<Card>
			<LocationIcon />
			<div>
				<h2 class="font-semibold">Indirizzo</h2>
				<p>Via Azzone Visconti, 33, 23900 Lecco LC, Italia</p>
			</div>
		</Card>
	</a>
	<a class="p-4" href="tel:0341363498">
		<Card>
			<PhoneIcon />
			<h2 class="font-semibold">Telefono</h2>
			<p>0341.363498</p>
		</Card></a
	>

	<a class="p-4" href="mailto:afinonlus@gmail.com">
		<Card>
			<EmailIcon />
			<h2 class="font-semibold">Email</h2>
			<p>afinonlus@gmail.com</p>
		</Card>
	</a>

	<a
		class="p-4"
		href="https://www.facebook.com/people/AFIN-Associazione-Famiglie-Ipo-Non-Vedenti/100090068238710/"
	>
		<Card>
			<InternetIcon />
			<h2 class="font-semibold">Facebook</h2>
			<p>Afin Associazione Famiglie Ipo Non Vedenti</p>
		</Card>
	</a>
</section>

<!-- Maps -->
<section>
	<Card>
		<div class="relative w-full pt-[56.25%]">
			<iframe
				class="absolute top-0 left-0 h-full w-full border-0"
				title="map"
				src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2779.044896139235!2d9.389908312032967!3d45.8504007709622!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47841d300b77c249%3A0xc5f094eced398a5a!2sVia%20Azzone%20Visconti%2C%2033%2C%2023900%20Lecco%20LC%2C%20Italy!5e0!3m2!1sen!2sus!4v1740184465399!5m2!1sen!2sus"
				width="1000"
				height="512"
				allowfullscreen
				loading="lazy"
				referrerpolicy="no-referrer-when-downgrade"
			></iframe>
		</div>
	</Card>
</section>
