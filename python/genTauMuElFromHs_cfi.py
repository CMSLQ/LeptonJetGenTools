import FWCore.ParameterSet.Config as cms

#HToLL: X=e/mu/tau
genTausFromHs = cms.EDProducer('GenMotherParticleSkimmer',
  InputTag            = cms.InputTag('genParticles'),
  MotherPDGIds        = cms.vint32( 25 ),
  MotherPDGIdsVetoed  = cms.vint32( ), 
  DaughterPDGIds      = cms.vint32( 15 ),                            
  DaughterPDGStatuses = cms.vint32( 2 ),
  StoreFinalStateOnly = cms.bool ( True )                                 
)
 
genMuonsFromHs = cms.EDProducer('GenMotherParticleSkimmer',
  InputTag            = cms.InputTag('genParticles'),
  MotherPDGIds        = cms.vint32( 25 ),
  MotherPDGIdsVetoed  = cms.vint32( 111, 213 ),
  DaughterPDGIds      = cms.vint32( 13 ),    
  DaughterPDGStatuses = cms.vint32( 1 ),
  StoreFinalStateOnly = cms.bool ( False )                                 
)

genElectronsFromHs = cms.EDProducer('GenMotherParticleSkimmer',
  InputTag            = cms.InputTag('genParticles'),
  MotherPDGIds        = cms.vint32( 25 ),
  MotherPDGIdsVetoed  = cms.vint32( 111, 213 ),                                        
  DaughterPDGIds      = cms.vint32( 11 ),    
  DaughterPDGStatuses = cms.vint32( 1 ),
  StoreFinalStateOnly = cms.bool ( False )                                 
)

