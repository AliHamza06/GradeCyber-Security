from django.urls import path
from . import views
from .views import(
    home,
    SmartContractAudit,
    BlockchainProtocolSecurity,
    PenetrationTesting,
    dAppAudit,
    CryptoWalletAudit,
    CrossChainBridgeAudit,
    BugBounty,
    ProofOfReservesAudit,
    CCSSAudit,
    TokenomicsAuditDesign,
    Solutions,
    SolutionsBSC,
    SolutionsPolygon,
    SolutionsNear,
    SolutionsAvalanche,
    SolutionsFantom,
    SolutionsAptosSmart,
    SolutionsSui,
    SolutionsOptimismContract,
    SolutionsZkSync,
    SolutionsArbitrum,
    SolutionsSolana,
    SolutionsPolkadot,
    SolutionsCosmos,
    SolutionsRadix,
    SolutionsLinea,
    SolutionsMetaMask,
    SolutionsOther,
    SolutionsSolidity,
    SolutionsRust,
    SolutionsMove,
    CompanyOurMission,
    CompanyAbout, # Partner With Grade
    Blogs,
    CompanyAboutProfit,
    Career,
)
urlpatterns = [
    path('', views.home, name="home"),
    path('SmartContractAudit/', views.SmartContractAudit, name="SmartContractAudit"),
    path('BlockchainProtocolSecurity/', views.BlockchainProtocolSecurity, name="BlockchainProtocolSecurity"),
    path('PenetrationTesting/', views.PenetrationTesting, name="PenetrationTesting"),
    path('dAppAudit/', views.dAppAudit, name="dAppAudit"),
    path('CryptoWalletAudit/', views.CryptoWalletAudit, name="CryptoWalletAudit"),
    path('CrossChainBridgeAudit/', views.CrossChainBridgeAudit, name="Cross-ChainBridgeAudit"),
    path('BugBounty/', views.BugBounty, name="BugBounty"),
    path('ProofOfReservesAudit/', views.ProofOfReservesAudit, name="ProofOfReservesAudit"),
    path('CCSSAudit/', views.CCSSAudit, name="CCSSAudit"),
    path('TokenomicsAuditDesign/', views.TokenomicsAuditDesign, name="TokenomicsAuditDesign"),
    path('Solutions/', views.Solutions, name="Solutions"),
    path('SolutionsBSC/', views.SolutionsBSC, name="SolutionsBSC"),
    path('SolutionsPolygon/', views.SolutionsPolygon, name="SolutionsPolygon"),
    path('SolutionsNear/', views.SolutionsNear, name="SolutionsNear"),
    path('SolutionsAvalanche/', views.SolutionsAvalanche, name="SolutionsAvalanche"),
    path('SolutionsFantom/', views.SolutionsFantom, name="SolutionsFantom"),
    path('SolutionsAptosSmart/', views.SolutionsAptosSmart, name="SolutionsAptosSmart"),
    path('SolutionsSui/', views.SolutionsSui, name="SolutionsSui"),
    path('SolutionsOptimismContract/', views.SolutionsOptimismContract, name="SolutionsOptimismContract"),
    path('SolutionsZkSync/', views.SolutionsZkSync, name="SolutionsZkSync"),
    path('SolutionsArbitrum/', views.SolutionsArbitrum, name="SolutionsArbitrum"),
    path('SolutionsSolana/', views.SolutionsSolana, name="SolutionsSolana"),
    path('SolutionsPolkadot/', views.SolutionsPolkadot, name="SolutionsPolkadot"),
    path('SolutionsCosmos/', views.SolutionsCosmos, name="SolutionsCosmos"),
    path('SolutionsRadix/', views.SolutionsRadix, name="SolutionsRadix"),
    path('SolutionsLinea/', views.SolutionsLinea, name="SolutionsLinea"),
    path('SolutionsMetaMask/', views.SolutionsMetaMask, name="SolutionsMetaMask"),
    path('SolutionsOther/', views.SolutionsOther, name="SolutionsOther"),
    path('SolutionsSolidity/', views.SolutionsSolidity, name="SolutionsSolidity"),
    path('SolutionsRust/', views.SolutionsRust, name="SolutionsRust"),
    path('SolutionsMove/', views.SolutionsMove, name="SolutionsMove"),
    path('CompanyOurMission/', views.CompanyOurMission, name="CompanyOurMission"),
    path('CompanyAbout/', views.CompanyAbout, name="CompanyAbout"),
    path('Blogs/', views.Blogs, name="Blogs"),
    path('CompanyAboutProfit/', views.CompanyAboutProfit, name="CompanyAboutProfit"),
    path('Career/', views.Career, name="Career"),
]