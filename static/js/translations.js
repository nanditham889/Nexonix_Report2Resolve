const translations = {
    en: {
        welcome: "Welcome, Bengaluru Citizen",
        hub_title: "Command Center",
        roads: "Roads & Highways",
        sanitation: "Sanitation",
        water: "Water Supply",
        electricity: "Electricity",
        report_title: "Report New Issue",
        submit_btn: "Submit Report"
    },
    kn: {
        welcome: "ಸ್ವಾಗತ, ಬೆಂಗಳೂರು ನಾಗರಿಕ",
        hub_title: "ಪ್ರಾಧಿಕಾರ ಕಮಾಂಡ್ ಸೆಂಟರ್",
        roads: "ರಸ್ತೆಗಳು",
        sanitation: "ನೈರ್ಮಲ್ಯ",
        water: "ನೀರು ಸರಬರಾಜು",
        electricity: "ವಿದ್ಯುತ್",
        report_title: "ಹೊಸ ದೂರು",
        submit_btn: "ಸಲ್ಲಿಸಿ"
    },
    hi: {
        welcome: "स्वागत है, बेंगलुरु नागरिक",
        hub_title: "कमांड सेंटर",
        roads: "सड़कें",
        sanitation: "स्वच्छता",
        water: "जल आपूर्ति",
        electricity: "बिजली",
        report_title: "नई शिकायत",
        submit_btn: "जमा करें"
    }
};

function changeLanguage(lang) {
    document.querySelectorAll('[data-key]').forEach(el => {
        const key = el.getAttribute('data-key');
        if (translations[lang][key]) el.innerText = translations[lang][key];
    });
    localStorage.setItem('selectedLang', lang);
}

document.addEventListener('DOMContentLoaded', () => {
    changeLanguage(localStorage.getItem('selectedLang') || 'en');
});