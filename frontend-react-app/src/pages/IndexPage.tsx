import { useCallback, useEffect, useMemo, useState, type FC } from 'react';

// MUI Components
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import { ThemeProvider, createTheme } from '@mui/material/styles'; // For custom theme if needed

// Custom Components
import MitsuisumitomoCardCard from '../components/MitsuisumitomoCardCard';
import RakutenBankCard from '../components/RakutenBankCard';
import SbiBenefitSystemCard from '../components/SbiBenefitSystemCard';
import SbiShinseiBankCard from '../components/SbiShinseiBankCard';
import SumishinSbiBankCard from '../components/SumishinSbiBankCard';
import TotalCard from '../components/TotalCard';

// Repositories
import { mitsuisumitomoCardRepository } from '../repositories/MitsuisumitomoCardRepository';
import { rakutenBankRepository } from '../repositories/RakutenBankRepository';
import { sbiBenefitSystemRepository } from '../repositories/SbiBenefitSystemRepository';
import { sbiShinseiBankRepository } from '../repositories/SbiShinseiBankRepository';
import { sumishinSbiBankRepository } from '../repositories/SumishinSbiBankRepository';

// Define types for state
interface TotalsState {
  rakutenBank: number;
  sbiShinseiBank: number;
  sumishinSbiBank: number;
  sbiBenefitSystem: number;
  smbcCard: number;
}

interface LoadingsState {
  rakutenBank: boolean;
  sbiShinseiBank: boolean;
  sumishinSbiBank: boolean;
  sbiBenefitSystem: boolean;
  smbcCard: boolean;
}

export const IndexPage: FC = () => {
  const [totals, setTotals] = useState<TotalsState>({
    rakutenBank: 0,
    sbiShinseiBank: 0,
    sumishinSbiBank: 0,
    sbiBenefitSystem: 0,
    smbcCard: 0,
  });

  const [loadings, setLoadings] = useState<LoadingsState>({
    rakutenBank: false,
    sbiShinseiBank: false,
    sbiBenefitSystem: false,
    sumishinSbiBank: false,
    smbcCard: false,
  });

  // Derived state for grand total and overall loading status
  const grandTotal = useMemo(() => {
    return Object.values(totals).reduce((acc, current) => acc + current, 0);
  }, [totals]);

  const isAnyLoading = useMemo(() => {
    return Object.values(loadings).some(loading => loading);
  }, [loadings]);

  // Initial data fetching
  useEffect(() => {
    const fetchInitialData = async () => {
      try {
        const [
          rakutenRes,
          sbiShinseiRes,
          sumishinSbiRes,
          sbiBenefitRes,
          smbcCardRes,
        ] = await Promise.allSettled([
          rakutenBankRepository.getLatest(),
          sbiShinseiBankRepository.getLatest(),
          sumishinSbiBankRepository.getLatest(),
          sbiBenefitSystemRepository.getLatest(),
          mitsuisumitomoCardRepository.getLatest(),
        ]);

        setTotals(prevTotals => ({
          ...prevTotals,
          rakutenBank: rakutenRes.status === 'fulfilled' ? rakutenRes.value.data.total : 0,
          sbiShinseiBank: sbiShinseiRes.status === 'fulfilled' ? sbiShinseiRes.value.data.total : 0,
          sumishinSbiBank: sumishinSbiRes.status === 'fulfilled' ? sumishinSbiRes.value.data.total : 0,
          sbiBenefitSystem: sbiBenefitRes.status === 'fulfilled' ? sbiBenefitRes.value.data.total : 0,
          smbcCard: smbcCardRes.status === 'fulfilled' ? (smbcCardRes.value.data.total ?? 0) : 0,
        }));
      } catch (error) {
        console.error("Error fetching initial data:", error);
        // Optionally, set all totals to 0 or display an error message
        setTotals({
            rakutenBank: 0,
            sbiShinseiBank: 0,
            sumishinSbiBank: 0,
            sbiBenefitSystem: 0,
            smbcCard: 0,
        });
      }
    };
    fetchInitialData();
  }, []);

  // WebSocket connection
  useEffect(() => {
    const ws = new WebSocket('ws://localhost:18080/mitsuisumitomo_bank');

    ws.onopen = () => {
      console.log('Connected to mitsuisumitomo_bank WebSocket');
      ws.send('Hello from frontend-react');
    };

    ws.onmessage = (event) => {
      console.log('WebSocket message received:', event.data);
      // Potentially update state based on message, if applicable
    };

    ws.onclose = () => {
      console.log('Disconnected from mitsuisumitomo_bank WebSocket');
    };

    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };

    return () => {
      ws.close(); // Cleanup on component unmount
    };
  }, []); // Empty dependency array ensures this runs once on mount and cleans up on unmount

  // Individual update handlers
  const createUpdateHandler = useCallback(
    async (
      repo: { update: () => Promise<any>; getLatest: () => Promise<{ data: { total: number | null } }> },
      key: keyof TotalsState
    ) => {
      setLoadings(prev => ({ ...prev, [key]: true }));
      try {
        const updateRes = await repo.update();
        // Check status of updateRes if necessary, original code checks for non-200
        if (updateRes.status !== 200 && updateRes.status !== 201 && updateRes.status !== 204) { // 204 for no content success
            console.error(`Failed to update ${key}: Status ${updateRes.status}`);
            // Potentially show an error to the user for this specific card
        }
        const latestRes = await repo.getLatest();
        setTotals(prev => ({ ...prev, [key]: latestRes.data.total ?? 0 }));
      } catch (error) {
        console.error(`Error updating ${key}:`, error);
        // Optionally keep old total or set to 0
      } finally {
        setLoadings(prev => ({ ...prev, [key]: false }));
      }
    },
    [] // No dependencies as it's a generic handler creator
  );

  const handleRakutenBankUpdate = useCallback(
    () => createUpdateHandler(rakutenBankRepository, 'rakutenBank'),
    [createUpdateHandler]
  );
  const handleSbiShinseiBankUpdate = useCallback(
    () => createUpdateHandler(sbiShinseiBankRepository, 'sbiShinseiBank'),
    [createUpdateHandler]
  );
  const handleSumishinSbiBankUpdate = useCallback(
    () => createUpdateHandler(sumishinSbiBankRepository, 'sumishinSbiBank'),
    [createUpdateHandler]
  );
  const handleSbiBenefitSystemUpdate = useCallback(
    () => createUpdateHandler(sbiBenefitSystemRepository, 'sbiBenefitSystem'),
    [createUpdateHandler]
  );
  const handleSmbcCardUpdate = useCallback(
    () => createUpdateHandler(mitsuisumitomoCardRepository, 'smbcCard'),
    [createUpdateHandler]
  );

  const handleAllUpdate = useCallback(async () => {
    // Set all to loading - though individual handlers also do this.
    // This provides immediate feedback on the TotalCard.
    // Note: isAnyLoading will be true from TotalCard's perspective
    // We are not setting individual loading states here to avoid multiple state updates.
    // The `isAnyLoading` prop for TotalCard will be derived from individual loading states.

    console.log("Updating all accounts...");
    try {
      await Promise.allSettled([
        handleRakutenBankUpdate(),
        handleSbiShinseiBankUpdate(),
        handleSumishinSbiBankUpdate(),
        handleSbiBenefitSystemUpdate(),
        handleSmbcCardUpdate(),
      ]);
    } catch (error) {
      console.error("Error during 'handleAllUpdate':", error);
    }
  }, [
    handleRakutenBankUpdate,
    handleSbiShinseiBankUpdate,
    handleSumishinSbiBankUpdate,
    handleSbiBenefitSystemUpdate,
    handleSmbcCardUpdate,
  ]);

  // Simple theme for consistent spacing, can be expanded
  const theme = createTheme({
    spacing: 8, // Default spacing factor
  });

  return (
    <ThemeProvider theme={theme}>
      <Container sx={{ py: 3 }}> {/* py: padding top/bottom, similar to q-page */}
        <Grid container spacing={3} justifyContent="space-evenly" alignItems="stretch"> {/* alignItems="stretch" to make cards same height if content differs */}
          <Grid xs={12} md={4} component="div">
            <TotalCard
              total={grandTotal}
              loading={isAnyLoading} // TotalCard loading reflects if ANY card is loading
              onClickUpdate={handleAllUpdate}
            />
          </Grid>
          <Grid xs={12} md={4} component="div">
            <RakutenBankCard
              total={totals.rakutenBank}
              loading={loadings.rakutenBank}
              onClickUpdate={handleRakutenBankUpdate}
            />
          </Grid>
          <Grid xs={12} md={4} component="div">
            <SbiShinseiBankCard
              total={totals.sbiShinseiBank}
              loading={loadings.sbiShinseiBank}
              onClickUpdate={handleSbiShinseiBankUpdate}
            />
          </Grid>
          <Grid xs={12} md={4} component="div">
            <SumishinSbiBankCard
              total={totals.sumishinSbiBank}
              loading={loadings.sumishinSbiBank}
              onClickUpdate={handleSumishinSbiBankUpdate}
            />
          </Grid>
          <Grid xs={12} md={4} component="div">
            <SbiBenefitSystemCard
              total={totals.sbiBenefitSystem}
              loading={loadings.sbiBenefitSystem}
              onClickUpdate={handleSbiBenefitSystemUpdate}
            />
          </Grid>
          <Grid xs={12} md={4} component="div">
            <MitsuisumitomoCardCard
              total={totals.smbcCard}
              loading={loadings.smbcCard}
              onClickUpdate={handleSmbcCardUpdate}
            />
          </Grid>
        </Grid>
      </Container>
    </ThemeProvider>
  );
};

export default IndexPage;
